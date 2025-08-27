@echo off
echo.
echo ============================================
echo   🎉 Emoji Translator AI - Lifetime Free!
echo ============================================
echo.
echo Setting up your lifetime free emoji translator...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Install requirements
echo 📦 Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Create static directory if it doesn't exist
if not exist "static" (
    mkdir static
    echo ✅ Created static directory
)

echo.
echo ============================================
echo   🚀 Starting Lifetime Free Service
echo ============================================
echo.
echo 🌐 Your emoji translator will be available at:
echo    http://localhost:8000
echo.
echo 📚 API documentation at:
echo    http://localhost:8000/docs
echo.
echo 💝 This service is completely FREE forever!
echo    No limits, no subscriptions, no accounts needed.
echo.
echo 🛑 Press Ctrl+C to stop the server
echo.

REM Start the free server
python api_free.py

pause
