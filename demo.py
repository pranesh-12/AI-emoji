#!/usr/bin/env python3
"""
Example script demonstrating Emoji Translator AI capabilities
Run this to see the translator in action with various examples
"""

from translator import EmojiTranslator
import json

def print_separator(title):
    """Print a nice separator with title."""
    print("\n" + "="*60)
    print(f" {title} ".center(60, "="))
    print("="*60)

def demonstrate_basic_translation():
    """Demonstrate basic translation functionality."""
    print_separator("BASIC TRANSLATION EXAMPLES")
    
    translator = EmojiTranslator()
    
    examples = [
        "Good morning! I love coffee and programming.",
        "This project is on fire! Let's break the ice.",
        "I'm over the moon about this amazing success.",
        "Time for a meeting at the office today.",
        "Feeling blue, need some music and chocolate.",
        "Let's spill the tea about this exciting news!",
        "Catch some z's after this long day of work.",
        "The team is burning the midnight oil on this deadline."
    ]
    
    for i, text in enumerate(examples, 1):
        result = translator.translate(text, density='medium', style='fun')
        print(f"{i}. Original: {text}")
        print(f"   Translated: {result}")
        print()

def demonstrate_styles():
    """Demonstrate different translation styles."""
    print_separator("TRANSLATION STYLES COMPARISON")
    
    translator = EmojiTranslator()
    text = "Good morning team! Let's have a productive meeting about our amazing project data."
    
    styles = ['fun', 'professional', 'meme']
    
    print(f"Original: {text}\n")
    
    for style in styles:
        result = translator.translate(text, style=style, density='medium')
        print(f"{style.upper():>12}: {result}")
    print()

def demonstrate_modes():
    """Demonstrate append vs replace modes."""
    print_separator("TRANSLATION MODES COMPARISON")
    
    translator = EmojiTranslator()
    text = "Happy cat loves coffee in the morning"
    
    print(f"Original: {text}\n")
    
    append_result = translator.translate(text, mode='append', density='heavy')
    replace_result = translator.translate(text, mode='replace', density='heavy')
    
    print(f"  APPEND MODE: {append_result}")
    print(f" REPLACE MODE: {replace_result}")
    print()

def demonstrate_density():
    """Demonstrate different density levels."""
    print_separator("DENSITY LEVELS COMPARISON")
    
    translator = EmojiTranslator()
    text = "I love programming with Python and drinking coffee while working on amazing projects"
    
    densities = ['light', 'medium', 'heavy']
    
    print(f"Original: {text}\n")
    
    for density in densities:
        result = translator.translate(text, density=density, style='fun')
        emoji_count = len(result) - len(text)
        print(f"{density.upper():>6} ({emoji_count:+3d} chars): {result}")
    print()

def demonstrate_sentiment():
    """Demonstrate sentiment detection and emoji addition."""
    print_separator("SENTIMENT DETECTION EXAMPLES")
    
    translator = EmojiTranslator()
    
    sentiment_examples = [
        ("This is absolutely amazing and wonderful!", "positive"),
        ("I'm frustrated and disappointed with this terrible situation.", "negative"),
        ("The weather is okay and the meeting is scheduled for tomorrow.", "neutral"),
        ("I love this fantastic project and the awesome team!", "positive"),
        ("This is awful, horrible, and completely disappointing.", "negative")
    ]
    
    for text, expected in sentiment_examples:
        detected = translator._detect_sentiment(text)
        result = translator.translate(text, add_sentiment=True, density='medium')
        print(f"Text: {text}")
        print(f"Expected: {expected} | Detected: {detected}")
        print(f"With sentiment: {result}")
        print()

def demonstrate_context_awareness():
    """Demonstrate context-aware emoji selection."""
    print_separator("CONTEXT-AWARE TRANSLATION")
    
    translator = EmojiTranslator()
    
    context_examples = [
        "The team is on fire with this project!",
        "Call the fire station immediately!",
        "Good morning sunshine, time to wake up!",
        "Good night moon, time for sleep.",
        "The sun is shining bright this morning.",
        "The moon looks beautiful tonight."
    ]
    
    for text in context_examples:
        result = translator.translate(text, density='heavy', style='fun')
        print(f"Original: {text}")
        print(f"Context-aware: {result}")
        print()

def demonstrate_custom_emojis():
    """Demonstrate loading custom emoji mappings."""
    print_separator("CUSTOM EMOJI MAPPINGS")
    
    print("Loading custom emojis from custom_emojis.json...")
    try:
        translator = EmojiTranslator(custom_emoji_file='custom_emojis.json')
        
        custom_examples = [
            "This Python code is awesome and amazing!",
            "I love machine learning and artificial intelligence.",
            "Working from home with my developer skills.",
            "Cryptocurrency and blockchain are trending topics.",
            "Climate change requires renewable energy solutions."
        ]
        
        for text in custom_examples:
            result = translator.translate(text, density='medium', style='fun')
            print(f"Original: {text}")
            print(f"With custom emojis: {result}")
            print()
            
    except FileNotFoundError:
        print("custom_emojis.json not found. Creating example...")
        
        example_custom = {
            "words": {
                "python": ["", "", ""],
                "awesome": ["", "", ""]
            },
            "phrases": {
                "machine learning": ""
            }
        }
        
        with open('example_custom_emojis.json', 'w', encoding='utf-8') as f:
            json.dump(example_custom, f, indent=2, ensure_ascii=False)
        
        translator = EmojiTranslator(custom_emoji_file='example_custom_emojis.json')
        result = translator.translate("Python is awesome for machine learning", density='heavy')
        print(f"Example with custom emojis: {result}")

def demonstrate_performance():
    """Demonstrate performance with various text lengths."""
    print_separator("PERFORMANCE DEMONSTRATION")
    
    import time
    
    translator = EmojiTranslator()
    
    # Test different text lengths
    test_cases = [
        ("Short", "Hello world!"),
        ("Medium", "Good morning! I love coffee and programming with Python. " * 5),
        ("Long", "This is a longer text to test performance with many words. " * 20),
        ("Very Long", "Performance test with repeated words and phrases. " * 100)
    ]
    
    for name, text in test_cases:
        start_time = time.time()
        result = translator.translate(text, density='medium', style='fun')
        end_time = time.time()
        
        processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"{name:>10} ({len(text):>4} chars): {processing_time:.2f}ms")
    print()

def main():
    """Run all demonstrations."""
    print(" EMOJI TRANSLATOR AI - DEMONSTRATION SCRIPT ")
    print("This script showcases all the advanced features of the Emoji Translator AI")
    
    try:
        demonstrate_basic_translation()
        demonstrate_styles()
        demonstrate_modes()
        demonstrate_density()
        demonstrate_sentiment()
        demonstrate_context_awareness()
        demonstrate_custom_emojis()
        demonstrate_performance()
        
        print_separator("DEMONSTRATION COMPLETE")
        print(" All features demonstrated successfully!")
        print("\nNext steps:")
        print("1. Try the CLI: python translator.py \"Your text here\"")
        print("2. Launch Web UI: streamlit run app_streamlit.py")
        print("3. Start API: python api.py")
        print("\nHappy emoji translating! ")
        
    except Exception as e:
        print(f"\n Error during demonstration: {e}")
        print("Make sure all required files are present and dependencies are installed.")

if __name__ == "__main__":
    main()
