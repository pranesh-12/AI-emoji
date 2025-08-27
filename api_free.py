from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from translator import EmojiTranslator
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Emoji Translator AI - Lifetime Free",
    description="Transform your text with intelligent emoji translation - Forever Free!",
    version="2.0.0"
)

# CORS configuration for web browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the translator
translator = EmojiTranslator()

class TranslationRequest(BaseModel):
    text: str
    style: str = "fun"
    density: str = "medium"
    mode: str = "append"
    add_sentiment: bool = True

class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    style: str
    density: str
    mode: str
    add_sentiment: bool
    status: str = "success"
    message: str = "Translation completed successfully! 🎉"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page"""
    return FileResponse('static/index.html')

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Emoji Translator AI",
        "version": "2.0.0",
        "plan": "Lifetime Free",
        "message": "Service is running perfectly! 🚀"
    }

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """
    Translate text to emoji-enhanced version
    
    This endpoint is completely free with no limits!
    """
    try:
        logger.info(f"Free translation request: {len(request.text)} characters")
        
        # Validate input
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        if len(request.text) > 10000:
            raise HTTPException(status_code=400, detail="Text too long (max 10,000 characters)")
        
        # Perform translation
        translated_text = translator.translate(
            text=request.text,
            style=request.style,
            density=request.density,
            mode=request.mode,
            add_sentiment=request.add_sentiment
        )
        
        logger.info("Free translation completed successfully")
        
        return TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            style=request.style,
            density=request.density,
            mode=request.mode,
            add_sentiment=request.add_sentiment,
            status="success",
            message="Translation completed successfully! 🎉 Thanks for using our lifetime free service!"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")

@app.get("/stats")
async def get_stats():
    """Get service statistics"""
    return {
        "service": "Emoji Translator AI",
        "plan": "Lifetime Free",
        "features": [
            "✅ Unlimited translations",
            "✅ All emoji styles available",
            "✅ Multiple density levels",
            "✅ Sentiment analysis",
            "✅ Replace or append modes",
            "✅ No daily limits",
            "✅ No account required",
            "✅ Open source friendly",
            "✅ Ad-supported revenue model"
        ],
        "limits": {
            "daily_translations": "Unlimited",
            "max_text_length": 10000,
            "rate_limit": "None",
            "api_access": "Free forever"
        },
        "support": {
            "donations": "https://buymeacoffee.com/emojitranslator",
            "github": "https://github.com/username/emoji-translator-ai",
            "share": "Help us grow by sharing with friends!"
        }
    }

@app.get("/examples")
async def get_examples():
    """Get example translations to showcase the service"""
    examples = [
        {
            "original": "Good morning! I am feeling great and ready for work.",
            "style": "fun",
            "density": "medium"
        },
        {
            "original": "Let's have coffee and discuss the project deadline.",
            "style": "professional", 
            "density": "light"
        },
        {
            "original": "I am over the moon about this amazing success!",
            "style": "meme",
            "density": "heavy"
        }
    ]
    
    results = []
    for example in examples:
        translated = translator.translate(
            text=example["original"],
            style=example["style"],
            density=example["density"],
            add_sentiment=True
        )
        results.append({
            "original": example["original"],
            "translated": translated,
            "style": example["style"],
            "density": example["density"]
        })
    
    return {"examples": results}

if __name__ == "__main__":
    print("🎉 Starting Emoji Translator AI - Lifetime Free Service!")
    print("🌐 Web interface will be available at: http://localhost:8000")
    print("📚 API documentation at: http://localhost:8000/docs")
    print("💝 This service is completely free forever!")
    
    uvicorn.run(
        "api_free:app",
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )
