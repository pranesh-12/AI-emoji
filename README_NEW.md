# 🎯 Emoji Translator AI

Transform your text with intelligent emoji translation! A modern web application that adds context-aware emojis to your text with multiple styles and modes.

## ✨ Features

- 🎨 **Multiple Styles**: Fun, Professional, and Meme modes
- 📊 **Density Control**: Light, Medium, or Heavy emoji density
- 🔄 **Translation Modes**: Append emojis to words or replace words with emojis
- 💫 **Sentiment Analysis**: Automatic sentiment emoji detection
- 🌐 **Web Interface**: Beautiful, responsive web application
- 🚀 **REST API**: Full-featured API for integration
- 📱 **Mobile Friendly**: Works great on all devices

## 🚀 Quick Start

### Option 1: Windows Batch File (Easiest)
1. Double-click `start_server.bat`
2. Wait for packages to install and server to start
3. Open your browser to `http://localhost:8000`

### Option 2: Python Command Line
```bash
# Install dependencies
pip install fastapi uvicorn[standard] pydantic python-multipart

# Start the server
python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

### Option 3: Python Launcher
```bash
python launch_web.py
```

## 🌐 Web Application

Once the server is running, open your browser to:
- **Main App**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Alternative**: http://localhost:8000/app

## 📖 API Usage

### Translate Text (POST)
```bash
curl -X POST "http://localhost:8000/translate" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "Good morning! I am feeling great and ready for work.",
       "style": "fun",
       "density": "medium",
       "mode": "append",
       "add_sentiment": true
     }'
```

### Quick Translation (GET)
```bash
curl "http://localhost:8000/translate?text=Hello world&style=fun&density=medium"
```

### Health Check
```bash
curl "http://localhost:8000/health"
```

## 🎨 Translation Options

### Styles
- **fun**: Playful and expressive emojis
- **professional**: Subtle and workplace-appropriate
- **meme**: Over-the-top and humorous

### Density Levels
- **light**: Minimal emoji usage
- **medium**: Balanced emoji distribution
- **heavy**: Emoji-rich text

### Modes
- **append**: Add emojis alongside words (e.g., "happy 😊")
- **replace**: Replace words with emojis (e.g., "😊")

## 📁 Project Structure

```
emoji-translator-ai/
├── api.py                 # FastAPI web server
├── translator.py          # Core emoji translation logic
├── static/
│   └── index.html        # Web frontend
├── start_server.bat      # Windows launcher
├── launch_web.py         # Python launcher
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🛠️ Core Components

### EmojiTranslator Class
The heart of the application with these methods:
- `translate()` - Main translation function
- `load_custom_emojis()` - Load custom emoji mappings
- `_detect_sentiment()` - Analyze text sentiment
- `_get_context_aware_emoji()` - Context-based emoji selection

### Web Interface
- Modern, responsive design
- Real-time translation
- Copy-to-clipboard functionality
- Pre-built examples
- Mobile-friendly interface

### REST API
- Full CORS support
- Comprehensive error handling
- Interactive documentation
- Multiple response formats

## 🔧 Advanced Usage

### Custom Emoji Mappings
Create a `custom_emojis.json` file:
```json
{
  "words": {
    "awesome": ["🔥", "💯", "⭐"],
    "coding": ["💻", "👨‍💻", "🔧"]
  },
  "phrases": {
    "let's go": "🚀",
    "well done": "👏"
  }
}
```

### Command Line Usage
```bash
# Direct translator usage
python translator.py "Hello world!" --style fun --density medium

# With custom emojis
python translator.py "Awesome coding session!" --custom-emojis custom_emojis.json
```

## 🌟 Examples

### Input
```
Good morning! I am feeling great and ready for work. Let's have coffee and discuss the project.
```

### Output (Fun Style, Medium Density)
```
Good morning! 🌅 I am feeling great 😊 and ready for work. 💼 Let's have coffee ☕ and discuss the project. 📋 😊
```

### Output (Professional Style, Light Density)
```
Good morning! 🌅 I am feeling great and ready for work. 💼 Let's have coffee and discuss the project.
```

### Output (Meme Style, Heavy Density)
```
Good morning! 🌅🌄☀️ I am feeling great 😊😁🤩 and ready for work. 💼👔💻 Let's have coffee ☕☕☕ and discuss the project. 📋📊📈 🤩🤩🤩
```

## 🐛 Troubleshooting

### Server Won't Start
1. Check if Python is installed: `python --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Check if port 8000 is available
4. Try a different port: `python -m uvicorn api:app --port 8001`

### Import Errors
```bash
# Reinstall dependencies
pip uninstall fastapi uvicorn pydantic
pip install fastapi uvicorn[standard] pydantic python-multipart
```

### CORS Issues
The API includes CORS headers for all origins. If you still have issues:
1. Check your browser's console for errors
2. Try accessing the API directly: `http://localhost:8000/docs`

## 📱 Mobile Usage

The web application is fully responsive and works great on mobile devices:
- Touch-friendly interface
- Optimized text input
- Easy copy-to-clipboard
- Vertical layout on small screens

## 🔮 Future Enhancements

- [ ] Multiple language support
- [ ] User accounts and saved translations
- [ ] Translation history
- [ ] Custom emoji packs
- [ ] Integration with messaging platforms
- [ ] Voice input support
- [ ] Emoji analytics

## 🤝 Contributing

Feel free to contribute by:
1. Adding new emoji mappings
2. Improving the web interface
3. Adding new translation modes
4. Enhancing the API
5. Writing tests

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Enjoy!

Have fun translating your text with emojis! 🎊✨🚀
