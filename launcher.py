#!/usr/bin/env python3
"""
Emoji Translator AI - Quick Launcher
Easy way to start any component of the Emoji Translator AI system
"""

import subprocess
import sys
import os
from pathlib import Path

def print_banner():
    """Print welcome banner."""
    banner = """
     ============================================== 
       EMOJI TRANSLATOR AI - QUICK LAUNCHER
     ============================================== 
    
    Transform your text with intelligent emoji translation!
    """
    print(banner)

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import fastapi
        import uvicorn
        return True
    except ImportError as e:
        print(f" Missing dependency: {e}")
        print("\n Please install dependencies first:")
        print("pip install -r requirements.txt")
        return False

def run_cli_demo():
    """Run CLI demonstration."""
    print("  Starting CLI Demo...")
    try:
        subprocess.run([sys.executable, "demo.py"], check=True)
    except subprocess.CalledProcessError:
        print(" Error running demo. Make sure demo.py exists.")
    except KeyboardInterrupt:
        print("\n  Demo stopped by user.")

def run_streamlit():
    """Launch Streamlit web interface."""
    print(" Starting Streamlit Web Interface...")
    print(" Will open at: http://localhost:8501")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app_streamlit.py"], check=True)
    except subprocess.CalledProcessError:
        print(" Error starting Streamlit. Make sure app_streamlit.py exists.")
    except KeyboardInterrupt:
        print("\n  Streamlit stopped by user.")

def run_fastapi():
    """Launch FastAPI server."""
    print(" Starting FastAPI Server...")
    print(" API will be available at: http://localhost:8000")
    print(" Documentation at: http://localhost:8000/docs")
    try:
        subprocess.run([sys.executable, "api.py"], check=True)
    except subprocess.CalledProcessError:
        print(" Error starting API server. Make sure api.py exists.")
    except KeyboardInterrupt:
        print("\n  API server stopped by user.")

def run_tests():
    """Run the test suite."""
    print(" Running Test Suite...")
    try:
        subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], check=True)
    except subprocess.CalledProcessError:
        print(" Some tests failed or pytest not installed.")
        print(" Install pytest: pip install pytest")
    except KeyboardInterrupt:
        print("\n  Tests stopped by user.")

def quick_translate():
    """Quick translation from command line input."""
    print(" Quick Translation Mode")
    print("Enter text to translate (or 'quit' to exit):")
    
    try:
        from translator import EmojiTranslator
        translator = EmojiTranslator()
        
        while True:
            text = input("\n Text: ").strip()
            if text.lower() in ['quit', 'exit', 'q']:
                break
            if not text:
                continue
                
            # Get user preferences
            print("\nChoose options (press Enter for defaults):")
            density = input("Density [light/medium/heavy] (default: medium): ").strip() or "medium"
            mode = input("Mode [append/replace] (default: append): ").strip() or "append"
            style = input("Style [fun/professional/meme] (default: fun): ").strip() or "fun"
            
            # Translate
            result = translator.translate(text, density=density, mode=mode, style=style, add_sentiment=True)
            
            print(f"\n Original:   {text}")
            print(f" Translated: {result}")
            
    except ImportError:
        print(" Could not import translator. Make sure translator.py exists.")
    except KeyboardInterrupt:
        print("\n Goodbye!")

def show_help():
    """Show help information."""
    help_text = """
 EMOJI TRANSLATOR AI - HELP

 WHAT IT DOES:
   Transforms regular text into emoji-enhanced versions using intelligent
   pattern matching, context awareness, and customizable styles.

  COMPONENTS:
   1. CLI Tool (translator.py) - Command-line interface
   2. Web UI (Streamlit) - Interactive web interface  
   3. API Server (FastAPI) - REST API for integrations
   4. Custom Mappings - Extend emoji database with JSON files

 FEATURES:
    Multi-word phrase detection ("on fire"  )
    Context-aware emoji selection
    3 styles: fun, professional, meme
    2 modes: append (word + emoji) or replace (emoji only)
    3 density levels: light, medium, heavy
    Sentiment detection and emoji addition
    Custom emoji mappings via JSON files
    Export and history features

 QUICK EXAMPLES:
   
   CLI Usage:
   python translator.py "Good morning! Time for coffee."
   python translator.py "I'm on fire!" --style meme --density heavy
   
   Python Code:
   from translator import EmojiTranslator
   t = EmojiTranslator()
   result = t.translate("Hello world!", style="fun")

 FILES:
   translator.py       - Core logic + CLI
   app_streamlit.py    - Web interface
   api.py             - REST API server
   custom_emojis.json - Custom emoji mappings
   demo.py            - Feature demonstration
   requirements.txt   - Dependencies
   tests/             - Unit tests

 LINKS:
    Web UI: http://localhost:8501 (after starting Streamlit)
    API Docs: http://localhost:8000/docs (after starting API)
    GitHub: [Your repository URL]

 SUPPORT:
    Run tests: python -m pytest tests/
    Check dependencies: pip install -r requirements.txt
    Report issues: [Your issue tracker URL]
   
 Have fun translating! 
    """
    print(help_text)

def main():
    """Main launcher interface."""
    print_banner()
    
    # Check if we're in the right directory
    if not Path("translator.py").exists():
        print(" translator.py not found!")
        print("Make sure you're in the emoji-translator-ai directory.")
        return
    
    while True:
        print("\n Choose an option:")
        print("1.  Run Feature Demo")
        print("2.  Launch Web Interface (Streamlit)")
        print("3.  Start API Server (FastAPI)")
        print("4.  Quick Translate")
        print("5.  Run Tests")
        print("6.  Show Help")
        print("7.  Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == "1":
            run_cli_demo()
        elif choice == "2":
            if check_dependencies():
                run_streamlit()
        elif choice == "3":
            if check_dependencies():
                run_fastapi()
        elif choice == "4":
            quick_translate()
        elif choice == "5":
            run_tests()
        elif choice == "6":
            show_help()
        elif choice == "7":
            print("\n Thanks for using Emoji Translator AI!")
            break
        else:
            print(" Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Goodbye! Thanks for using Emoji Translator AI!")
