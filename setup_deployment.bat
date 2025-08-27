@echo off
echo 🚀 Emoji Translator AI - Deployment Setup
echo ============================================
echo.

REM Create deployment directory
if not exist "deployment" mkdir deployment
cd deployment

echo 📦 Setting up deployment files...

REM Create Dockerfile for containerized deployment
echo Creating Dockerfile...
(
echo FROM python:3.11-slim
echo.
echo WORKDIR /app
echo.
echo COPY requirements.txt .
echo RUN pip install --no-cache-dir -r requirements.txt
echo.
echo COPY . .
echo.
echo EXPOSE 8000
echo.
echo CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
) > Dockerfile

REM Create docker-compose.yml
echo Creating docker-compose.yml...
(
echo version: '3.8'
echo services:
echo   emoji-translator:
echo     build: .
echo     ports:
echo       - "8000:8000"
echo     environment:
echo       - PORT=8000
echo     restart: unless-stopped
) > docker-compose.yml

REM Create Heroku Procfile
echo Creating Procfile for Heroku...
echo web: python -m uvicorn api:app --host 0.0.0.0 --port $PORT > Procfile

REM Create Railway deployment config
echo Creating railway.toml...
(
echo [build]
echo builder = "NIXPACKS"
echo.
echo [deploy]
echo startCommand = "python -m uvicorn api:app --host 0.0.0.0 --port $PORT"
echo.
echo [env]
echo PYTHON_VERSION = "3.11"
) > railway.toml

REM Create Render deployment config
echo Creating render.yaml...
(
echo services:
echo   - type: web
echo     name: emoji-translator-ai
echo     env: python
echo     buildCommand: pip install -r requirements.txt
echo     startCommand: python -m uvicorn api:app --host 0.0.0.0 --port $PORT
echo     envVars:
echo       - key: PYTHON_VERSION
echo         value: 3.11
) > render.yaml

echo.
echo ✅ Deployment files created successfully!
echo.
echo 📋 Next Steps:
echo 1. Choose your hosting platform:
echo    - Heroku (Free tier available)
echo    - Railway (Free tier available)
echo    - Render (Free tier available)
echo    - DigitalOcean App Platform
echo    - Google Cloud Run
echo    - AWS App Runner
echo.
echo 2. Follow the platform-specific instructions in DEPLOYMENT_GUIDE.md
echo.
pause
