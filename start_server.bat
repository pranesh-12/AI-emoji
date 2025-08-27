@echo off
echo 🎯 Emoji Translator AI - Web Application Launcher
echo ============================================================
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo ✅ Python is available
echo.

REM Install required packages
echo 📦 Installing required packages...
python -m pip install fastapi uvicorn[standard] pydantic python-multipart

if errorlevel 1 (
    echo ❌ Failed to install packages
    pause
    exit /b 1
)

echo ✅ All packages installed successfully
echo.

echo 🚀 Starting Emoji Translator AI Web Server...
echo.
echo 📍 Server will be available at: http://localhost:8000
echo 📖 API Documentation at: http://localhost:8000/docs
echo 🔄 Press Ctrl+C to stop the server
echo.

REM Start the FastAPI server
python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload

echo.
echo 👋 Server stopped. Press any key to exit...
pause >nul
