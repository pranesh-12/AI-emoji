#!/usr/bin/env python3
"""
Emoji Translator AI - Web Application Launcher
Easy-to-use launcher for the complete web application
"""

import os
import sys
import time
import subprocess
import webbrowser
from pathlib import Path

def check_requirements():
    """Check if required packages are installed."""
    try:
        import fastapi
        import uvicorn
        import pydantic
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        return False

def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "fastapi", "uvicorn[standard]", "pydantic", "python-multipart"
        ])
        print("✅ Successfully installed all packages")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        return False

def start_server():
    """Start the FastAPI server."""
    print("🚀 Starting Emoji Translator AI Web Server...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API Documentation at: http://localhost:8000/docs")
    print("🔄 Press Ctrl+C to stop the server")
    
    try:
        # Change to the directory containing this script
        script_dir = Path(__file__).parent.absolute()
        os.chdir(script_dir)
        
        # Start the server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "api:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except FileNotFoundError:
        print("❌ Could not find uvicorn. Please install it with: pip install uvicorn[standard]")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def open_browser():
    """Open the web application in the default browser."""
    time.sleep(2)  # Wait for server to start
    try:
        webbrowser.open("http://localhost:8000")
        print("🌐 Opened web application in your default browser")
    except Exception as e:
        print(f"⚠️ Could not open browser automatically: {e}")
        print("💡 Manually open: http://localhost:8000")

def main():
    """Main launcher function."""
    print("🎯 Emoji Translator AI - Web Application Launcher")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not Path("api.py").exists():
        print("❌ Could not find api.py. Make sure you're in the project directory.")
        return
    
    if not Path("translator.py").exists():
        print("❌ Could not find translator.py. Make sure you're in the project directory.")
        return
    
    # Check and install requirements
    if not check_requirements():
        print("\n📦 Installing missing packages...")
        if not install_requirements():
            print("❌ Could not install required packages. Please install manually:")
            print("   pip install fastapi uvicorn[standard] pydantic python-multipart")
            return
    
    print("\n✅ Everything is ready!")
    print("\n🚀 Choose an option:")
    print("1. Start web server (recommended)")
    print("2. Start web server and open browser")
    print("3. Exit")
    
    try:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            start_server()
        elif choice == "2":
            # Start server in background and open browser
            import threading
            server_thread = threading.Thread(target=start_server)
            server_thread.daemon = True
            server_thread.start()
            open_browser()
            
            # Keep the main thread alive
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n👋 Shutting down...")
        elif choice == "3":
            print("👋 Goodbye!")
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")
    
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
