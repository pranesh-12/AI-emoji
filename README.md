#  Emoji Translator AI 

An advanced Python-based emoji translation system that intelligently transforms text with contextual emojis. Features multiple translation modes, styles, and output formats including CLI, Web UI, and REST API.

##  Features

### Core Translation Logic
- **Phrase Pattern Matching**: Detects multi-word phrases like "on fire"  , "good morning"  
- **Comprehensive Emoji Map**: 200+ individual words with contextual emoji mappings
- **Smart Context Awareness**: Selects appropriate emojis based on surrounding words
- **Density Control**: Light, medium, or heavy emoji frequency
- **Translation Modes**:
  - **Append Mode**: Keep original word + emoji (`coffee`)
  - **Replace Mode**: Replace word with emoji only (``)
- **Sentiment Sprinkle**: Optional emotion-based emojis at the end

### Advanced Features
- **Custom Emoji Mappings**: Load additional emojis from JSON file
- **Multiple Output Styles**:
  - `fun`  Casual with variety of emojis
  - `professional`  Subtle, work-appropriate emojis
  - `meme`  Extra-heavy emoji spam with exaggerated replacements
- **Context-Aware Translation**: Time-aware and phrase-context emoji selection
- **Fast & Lightweight**: No heavy ML models, pure Python with regex
- **Export Options**: Save translations to text/JSON files
- **Translation History**: Keeps track of recent translations

##  Quick Start

### Installation

```bash
# Clone or download the project
cd emoji-translator-ai

# Install dependencies
pip install -r requirements.txt
```

### CLI Usage

```bash
# Basic translation
python translator.py "Good morning! I love programming and coffee!"

# Advanced options
python translator.py "I'm on fire today!" --density heavy --mode replace --style meme --sentiment

# Save translation
python translator.py "Hello world" --save output.txt

# Use custom emojis
python translator.py "Amazing project" --custom-emojis custom_emojis.json
```

### Web UI (Streamlit)

```bash
# Launch interactive web interface
streamlit run app_streamlit.py
```

Visit `http://localhost:8501` for the web interface with:
- Real-time translation preview
- Emoji density slider
- Style selection dropdown
- Translation history
- Export functionality

### API Server (FastAPI)

```bash
# Start API server
python api.py
```

Visit `http://localhost:8000` for API documentation.

**API Examples:**

```bash
# POST request
curl -X POST "http://localhost:8000/translate" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love programming!", "style": "fun", "density": "medium"}'

# GET request (quick translation)
curl "http://localhost:8000/translate?text=Hello world&style=meme&density=heavy"

# Get random example
curl "http://localhost:8000/random"
```

##  Project Structure

```
emoji-translator-ai/
 translator.py          # Core translation logic + CLI
 app_streamlit.py       # Streamlit web interface
 api.py                 # FastAPI REST server
 custom_emojis.json     # Custom emoji mappings
 requirements.txt       # Python dependencies
 tests/
    test_translator.py # Unit tests
 README.md             # This file
```

##  Usage Examples

### Different Styles

```python
from translator import EmojiTranslator

translator = EmojiTranslator()

text = "Good morning! Time for coffee and work."

# Fun style
fun = translator.translate(text, style='fun')
# Output: "Good morning! Time for coffee and work."

# Professional style  
prof = translator.translate(text, style='professional')
# Output: "Good morning! Time for coffee and work."

# Meme style
meme = translator.translate(text, style='meme', density='heavy')
# Output: "Good morning! Time for coffee and work!"
```

### Translation Modes

```python
# Append mode (default)
append = translator.translate("Happy cat", mode='append')
# Output: "Happy cat"

# Replace mode
replace = translator.translate("Happy cat", mode='replace')  
# Output: " "
```

### Density Levels

```python
text = "I love programming with Python"

# Light density (30% chance per word)
light = translator.translate(text, density='light')

# Medium density (60% chance per word)  
medium = translator.translate(text, density='medium')

# Heavy density (90% chance per word)
heavy = translator.translate(text, density='heavy')
```

##  Customization

### Custom Emoji Mappings

Create a `custom_emojis.json` file:

```json
{
  "words": {
    "awesome": ["", "", ""],
    "python": ["", "", ""]
  },
  "phrases": {
    "machine learning": "",
    "data science": ""
  }
}
```

Load custom emojis:

```python
translator = EmojiTranslator(custom_emoji_file='custom_emojis.json')
```

##  Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_translator.py::TestEmojiTranslator::test_phrase_detection -v

# Run with coverage
pip install pytest-cov
python -m pytest tests/ --cov=translator --cov-report=html
```

##  API Reference

### Core Translator Class

```python
class EmojiTranslator:
    def __init__(self, custom_emoji_file: Optional[str] = None)
    
    def translate(self, text: str, density: str = 'medium', 
                 mode: str = 'append', style: str = 'fun', 
                 add_sentiment: bool = False) -> str
```

### REST API Endpoints

- `POST /translate` - Translate text with full options
- `GET /translate?text=...` - Quick translation via query params
- `GET /health` - API health check
- `GET /info` - Emoji database information
- `GET /examples` - Example translations
- `GET /random` - Random translation example

##  Web UI Features

- **Real-time Preview**: See translations as you type
- **Interactive Controls**: Sliders and dropdowns for all options
- **Translation History**: View and manage past translations
- **Export Options**: Download as TXT or JSON
- **Custom Emoji Upload**: Upload your own emoji mappings
- **Statistics Display**: Character counts and emoji metrics

##  Performance

- **Lightning Fast**: Processes text instantly using regex patterns
- **Memory Efficient**: Lightweight with no heavy dependencies
- **Scalable**: Handles long texts efficiently
- **Self-Contained**: No external API calls required

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8

# Run tests
python -m pytest

# Format code
black *.py

# Lint code
flake8 *.py
```

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Support

-  Check the `/docs` endpoint when running the API server
-  Report bugs by opening an issue
-  Request features by opening an issue
-  Contact: [your-email@example.com]

##  Acknowledgments

- Emoji data inspired by Unicode Emoji Standard
- Built with love using Python, Streamlit, and FastAPI
- Thanks to the open-source community for amazing tools

---

**Made with  and lots of **

*Transform your text into emoji-rich expressions! *
