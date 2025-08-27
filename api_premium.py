#!/usr/bin/env python3
"""
Emoji Translator AI - Enhanced API with Monetization Features
"""

from fastapi import FastAPI, HTTPException, Query, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn
import json
from datetime import datetime, timedelta
from pathlib import Path
from translator import EmojiTranslator
import hashlib
import uuid

# Initialize FastAPI app
app = FastAPI(
    title="Emoji Translator AI - Premium",
    description="Transform text with intelligent emoji translation - Now with Premium Features!",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize translator
translator = EmojiTranslator()

# In-memory storage (use database in production)
user_usage = {}
api_keys = {}
premium_users = set()

# Pricing plans
PRICING_PLANS = {
    "free": {"daily_limit": 100, "features": ["basic_translation"], "price": 0},
    "premium": {"daily_limit": 1000, "features": ["all_styles", "premium_emojis", "analytics"], "price": 4.99},
    "pro": {"daily_limit": 10000, "features": ["unlimited", "api_access", "custom_branding"], "price": 19.99},
    "enterprise": {"daily_limit": 100000, "features": ["white_label", "priority_support", "custom_features"], "price": 99.99}
}

# Pydantic models
class TranslationRequest(BaseModel):
    text: str
    density: Optional[str] = "medium"
    mode: Optional[str] = "append"
    style: Optional[str] = "fun"
    add_sentiment: Optional[bool] = False

class PremiumTranslationRequest(TranslationRequest):
    api_key: Optional[str] = None
    premium_style: Optional[str] = None

class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    settings: Dict[str, Any]
    timestamp: str
    usage_info: Dict[str, Any]

class UsageStats(BaseModel):
    daily_usage: int
    monthly_usage: int
    plan: str
    remaining_today: int

def get_user_id(request) -> str:
    """Generate a unique user ID from request IP."""
    # In production, use proper user authentication
    user_ip = getattr(request.client, 'host', 'unknown')
    return hashlib.md5(user_ip.encode()).hexdigest()

def check_usage_limit(user_id: str, plan: str = "free") -> Dict[str, Any]:
    """Check if user has exceeded their usage limit."""
    today = datetime.now().date().isoformat()
    
    if user_id not in user_usage:
        user_usage[user_id] = {"daily": {}, "monthly": {}}
    
    daily_usage = user_usage[user_id]["daily"].get(today, 0)
    plan_limit = PRICING_PLANS[plan]["daily_limit"]
    
    return {
        "usage": daily_usage,
        "limit": plan_limit,
        "remaining": max(0, plan_limit - daily_usage),
        "exceeded": daily_usage >= plan_limit
    }

def increment_usage(user_id: str):
    """Increment user's daily usage."""
    today = datetime.now().date().isoformat()
    
    if user_id not in user_usage:
        user_usage[user_id] = {"daily": {}, "monthly": {}}
    
    user_usage[user_id]["daily"][today] = user_usage[user_id]["daily"].get(today, 0) + 1

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main web application."""
    return FileResponse('static/index.html')

@app.get("/pricing")
async def get_pricing():
    """Get pricing information."""
    return {
        "plans": PRICING_PLANS,
        "features_comparison": {
            "free": "Perfect for personal use",
            "premium": "Great for content creators",
            "pro": "Ideal for businesses",
            "enterprise": "Custom solutions"
        }
    }

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """Translate text with usage tracking."""
    # For demo purposes, using a simple IP-based user ID
    user_id = "demo_user"  # In production, get from authenticated user
    
    # Check usage limits
    usage_info = check_usage_limit(user_id, "free")
    
    if usage_info["exceeded"]:
        raise HTTPException(
            status_code=429,
            detail={
                "error": "Daily limit exceeded",
                "message": "Upgrade to Premium for unlimited translations",
                "upgrade_url": "/pricing"
            }
        )
    
    # Perform translation
    try:
        result = translator.translate(
            text=request.text,
            density=request.density,
            mode=request.mode,
            style=request.style,
            add_sentiment=request.add_sentiment
        )
        
        # Increment usage
        increment_usage(user_id)
        
        # Update usage info
        updated_usage = check_usage_limit(user_id, "free")
        
        return TranslationResponse(
            original_text=request.text,
            translated_text=result,
            settings={
                "density": request.density,
                "mode": request.mode,
                "style": request.style,
                "add_sentiment": request.add_sentiment
            },
            timestamp=datetime.now().isoformat(),
            usage_info={
                "plan": "free",
                "daily_usage": updated_usage["usage"],
                "daily_limit": updated_usage["limit"],
                "remaining_today": updated_usage["remaining"]
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")

@app.post("/premium/translate")
async def premium_translate(request: PremiumTranslationRequest):
    """Premium translation with enhanced features."""
    # Verify API key or premium subscription
    api_key = request.api_key
    if api_key and api_key in api_keys:
        plan = api_keys[api_key]["plan"]
    else:
        plan = "free"
    
    user_id = "premium_user" if plan != "free" else "demo_user"
    
    # Check usage limits
    usage_info = check_usage_limit(user_id, plan)
    
    if usage_info["exceeded"] and plan == "free":
        raise HTTPException(
            status_code=429,
            detail="Upgrade to Premium for unlimited translations"
        )
    
    # Enhanced translation for premium users
    enhanced_styles = {
        "business": "professional with enhanced vocabulary",
        "creative": "artistic with unique emoji combinations",
        "social": "optimized for social media engagement"
    }
    
    style = request.premium_style if request.premium_style in enhanced_styles else request.style
    
    result = translator.translate(
        text=request.text,
        density=request.density,
        mode=request.mode,
        style=style,
        add_sentiment=request.add_sentiment
    )
    
    if plan != "free":
        increment_usage(user_id)
    
    return {
        "original_text": request.text,
        "translated_text": result,
        "plan": plan,
        "premium_features_used": plan != "free",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/usage")
async def get_usage_stats():
    """Get user usage statistics."""
    user_id = "demo_user"
    today = datetime.now().date().isoformat()
    
    daily_usage = user_usage.get(user_id, {}).get("daily", {}).get(today, 0)
    
    return UsageStats(
        daily_usage=daily_usage,
        monthly_usage=sum(user_usage.get(user_id, {}).get("daily", {}).values()),
        plan="free",
        remaining_today=max(0, 100 - daily_usage)
    )

@app.post("/generate-api-key")
async def generate_api_key(plan: str = "premium"):
    """Generate API key for premium users."""
    if plan not in PRICING_PLANS:
        raise HTTPException(status_code=400, detail="Invalid plan")
    
    api_key = str(uuid.uuid4())
    api_keys[api_key] = {
        "plan": plan,
        "created": datetime.now().isoformat(),
        "usage": 0
    }
    
    return {
        "api_key": api_key,
        "plan": plan,
        "price": PRICING_PLANS[plan]["price"],
        "features": PRICING_PLANS[plan]["features"]
    }

@app.get("/analytics")
async def get_analytics():
    """Get usage analytics (for premium users)."""
    total_translations = sum(
        sum(user_data.get("daily", {}).values()) 
        for user_data in user_usage.values()
    )
    
    active_users = len([
        user_id for user_id, data in user_usage.items()
        if any(data.get("daily", {}).values())
    ])
    
    return {
        "total_translations": total_translations,
        "active_users": active_users,
        "premium_users": len(premium_users),
        "revenue_potential": {
            "daily": f"${active_users * 0.16:.2f}",  # Based on average conversion
            "monthly": f"${active_users * 4.99 * 0.03:.2f}",  # 3% conversion rate
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0",
        "features": ["monetization", "usage_tracking", "premium_api"]
    }

# Marketing endpoints
@app.get("/demo")
async def demo_translation():
    """Demo translation for marketing."""
    demo_text = "Hello world! I'm excited about this amazing project!"
    result = translator.translate(demo_text, density="medium", style="fun", add_sentiment=True)
    
    return {
        "demo": True,
        "original": demo_text,
        "translated": result,
        "message": "Try it yourself at our website!"
    }

if __name__ == "__main__":
    print("🚀 Starting Emoji Translator AI - Premium Edition")
    print("💰 Monetization features enabled")
    print("📊 Analytics tracking active")
    print("🔑 API key generation ready")
    print("\n🌐 Access your application:")
    print("   Main App: http://localhost:8000")
    print("   API Docs: http://localhost:8000/docs")
    print("   Pricing: http://localhost:8000/pricing")
    print("   Analytics: http://localhost:8000/analytics")
    
    uvicorn.run(
        "api_premium:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
