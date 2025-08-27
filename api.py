#!/usr/bin/env python3
"""
Emoji Translator AI - FastAPI Server
RESTful API for emoji translation services
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn
import json
from datetime import datetime
from pathlib import Path
from translator import EmojiTranslator

# Initialize FastAPI app
app = FastAPI(
    title="Emoji Translator AI",
    description="Transform text with intelligent emoji translation",
    version="1.0.0",
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

# Pydantic models for request/response
class TranslationRequest(BaseModel):
    text: str
    density: Optional[str] = "medium"
    mode: Optional[str] = "append"
    style: Optional[str] = "fun"
    add_sentiment: Optional[bool] = False

class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    settings: Dict[str, Any]
    timestamp: str
    statistics: Dict[str, int]

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str

class EmojiInfoResponse(BaseModel):
    total_words: int
    total_phrases: int
    available_styles: list
    available_modes: list
    available_densities: list

# API Routes

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main web application."""
    return FileResponse('static/index.html')

@app.get("/app", response_class=HTMLResponse)
async def app_page():
    """Alternative route to serve the web application."""
    return FileResponse('static/index.html')

@app.get("/api", response_class=HTMLResponse)
async def api_docs():
    """Root endpoint with API documentation."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emoji Translator AI - API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            .container { max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; }
            h1 { color: #FFD700; text-align: center; }
            .endpoint { background: rgba(255,255,255,0.2); padding: 15px; margin: 10px 0; border-radius: 8px; }
            .method { color: #4CAF50; font-weight: bold; }
            code { background: rgba(0,0,0,0.3); padding: 2px 6px; border-radius: 4px; }
            a { color: #FFD700; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Emoji Translator AI - API </h1>
            <p>Welcome to the Emoji Translator AI REST API! Transform your text with intelligent emoji translation.</p>
            
            <h2> Available Endpoints:</h2>
            
            <div class="endpoint">
                <p><span class="method">POST</span> <code>/translate</code> - Translate text with emojis</p>
                <p>Request body: <code>{"text": "your text", "style": "fun", "density": "medium"}</code></p>
            </div>
            
            <div class="endpoint">
                <p><span class="method">GET</span> <code>/translate</code> - Quick translation via query parameters</p>
                <p>Example: <code>/translate?text=Hello world&style=meme&density=heavy</code></p>
            </div>
            
            <div class="endpoint">
                <p><span class="method">GET</span> <code>/health</code> - API health check</p>
            </div>
            
            <div class="endpoint">
                <p><span class="method">GET</span> <code>/info</code> - Get emoji database information</p>
            </div>
            
            <h2> Interactive Documentation:</h2>
            <p>
                 <a href="/docs">Swagger UI Documentation</a><br>
                 <a href="/redoc">ReDoc Documentation</a>
            </p>
            
            <h2> Example Usage:</h2>
            <p><strong>cURL POST example:</strong></p>
            <code style="display: block; padding: 10px; margin: 10px 0;">
curl -X POST "http://localhost:8000/translate" \\<br>
&nbsp;&nbsp;&nbsp;&nbsp;-H "Content-Type: application/json" \\<br>
&nbsp;&nbsp;&nbsp;&nbsp;-d '{"text": "I love programming!", "style": "fun", "density": "medium"}'
            </code>
            
            <p><strong>Python requests example:</strong></p>
            <code style="display: block; padding: 10px; margin: 10px 0;">
import requests<br><br>
response = requests.post(<br>
&nbsp;&nbsp;&nbsp;&nbsp;"http://localhost:8000/translate",<br>
&nbsp;&nbsp;&nbsp;&nbsp;json={"text": "Good morning! Time for coffee", "style": "fun"}<br>
)<br>
print(response.json())
            </code>
        </div>
    </body>
    </html>
    """

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )

@app.get("/info", response_model=EmojiInfoResponse)
async def get_emoji_info():
    """Get information about the emoji database."""
    return EmojiInfoResponse(
        total_words=len(translator.emoji_map),
        total_phrases=len(translator.phrase_patterns),
        available_styles=["fun", "professional", "meme"],
        available_modes=["append", "replace"],
        available_densities=["light", "medium", "heavy"]
    )

@app.post("/translate", response_model=TranslationResponse)
async def translate_text_post(request: TranslationRequest):
    """
    Translate text with emojis using POST method.
    
    - **text**: The text to translate (required)
    - **density**: Emoji density level - light, medium, or heavy (default: medium)
    - **mode**: Translation mode - append or replace (default: append)
    - **style**: Output style - fun, professional, or meme (default: fun)
    - **add_sentiment**: Whether to add sentiment emoji at the end (default: false)
    """
    try:
        # Validate inputs
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        if request.density not in ["light", "medium", "heavy"]:
            raise HTTPException(status_code=400, detail="Density must be 'light', 'medium', or 'heavy'")
        
        if request.mode not in ["append", "replace"]:
            raise HTTPException(status_code=400, detail="Mode must be 'append' or 'replace'")
        
        if request.style not in ["fun", "professional", "meme"]:
            raise HTTPException(status_code=400, detail="Style must be 'fun', 'professional', or 'meme'")
        
        # Perform translation
        translated_text = translator.translate(
            text=request.text,
            density=request.density,
            mode=request.mode,
            style=request.style,
            add_sentiment=request.add_sentiment
        )
        
        # Calculate statistics
        original_length = len(request.text)
        translated_length = len(translated_text)
        emoji_difference = translated_length - original_length
        
        return TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            settings={
                "density": request.density,
                "mode": request.mode,
                "style": request.style,
                "add_sentiment": request.add_sentiment
            },
            timestamp=datetime.now().isoformat(),
            statistics={
                "original_length": original_length,
                "translated_length": translated_length,
                "character_difference": emoji_difference,
                "estimated_emojis_added": max(0, emoji_difference)
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.get("/translate", response_model=TranslationResponse)
async def translate_text_get(
    text: str = Query(..., description="Text to translate"),
    density: str = Query("medium", description="Emoji density: light, medium, heavy"),
    mode: str = Query("append", description="Translation mode: append, replace"),
    style: str = Query("fun", description="Output style: fun, professional, meme"),
    add_sentiment: bool = Query(False, description="Add sentiment emoji at the end")
):
    """
    Translate text with emojis using GET method with query parameters.
    Useful for quick translations and testing.
    """
    # Create request object and reuse POST logic
    request = TranslationRequest(
        text=text,
        density=density,
        mode=mode,
        style=style,
        add_sentiment=add_sentiment
    )
    return await translate_text_post(request)

@app.get("/examples")
async def get_examples():
    """Get example translations demonstrating different styles and modes."""
    example_text = "Good morning! I love coffee and programming. This project is on fire!"
    
    examples = []
    
    for style in ["fun", "professional", "meme"]:
        for mode in ["append", "replace"]:
            for density in ["light", "medium", "heavy"]:
                translated = translator.translate(
                    text=example_text,
                    density=density,
                    mode=mode,
                    style=style,
                    add_sentiment=True
                )
                
                examples.append({
                    "original": example_text,
                    "translated": translated,
                    "settings": {
                        "style": style,
                        "mode": mode,
                        "density": density,
                        "add_sentiment": True
                    }
                })
    
    return {"examples": examples}

@app.get("/random")
async def random_translation():
    """Get a random translation example."""
    import random
    
    sample_texts = [
        "Hello world! How are you today?",
        "I'm feeling great and ready for work!",
        "Time for lunch and then a meeting",
        "Programming is awesome and fun",
        "Good night, see you tomorrow!",
        "This coffee is amazing",
        "Let's break the ice and have some fun",
        "The project deadline is tomorrow",
        "I'm over the moon about this success",
        "Feeling blue today, need some music"
    ]
    
    text = random.choice(sample_texts)
    density = random.choice(["light", "medium", "heavy"])
    mode = random.choice(["append", "replace"])
    style = random.choice(["fun", "professional", "meme"])
    
    translated = translator.translate(
        text=text,
        density=density,
        mode=mode,
        style=style,
        add_sentiment=True
    )
    
    return {
        "original": text,
        "translated": translated,
        "settings": {
            "density": density,
            "mode": mode,
            "style": style,
            "add_sentiment": True
        },
        "timestamp": datetime.now().isoformat()
    }

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {"error": "Endpoint not found", "message": "Check /docs for available endpoints"}

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {"error": "Internal server error", "message": "Something went wrong on our end"}

def run_server():
    """Run the FastAPI server."""
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    print(" Starting Emoji Translator AI API Server...")
    print(" API Documentation: http://localhost:8000/docs")
    print(" Server: http://localhost:8000")
    run_server()
