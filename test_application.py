#!/usr/bin/env python3
"""
Test script to verify the Emoji Translator AI web application is working correctly
"""

import requests
import json
import time

def test_api_endpoint():
    """Test the main API endpoint"""
    url = "http://localhost:8000/translate"
    
    test_data = {
        "text": "Good morning! I am feeling great and ready for work. Let's have coffee and discuss the project.",
        "style": "fun",
        "density": "medium",
        "mode": "append",
        "add_sentiment": True
    }
    
    try:
        print("🧪 Testing API endpoint...")
        response = requests.post(url, json=test_data, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Test Successful!")
            print(f"📝 Original: {result['original_text']}")
            print(f"🎯 Translated: {result['translated_text']}")
            print(f"⚙️ Settings: {result['settings']}")
            return True
        else:
            print(f"❌ API Test Failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Server is not running or not accessible")
        print("💡 Make sure to run: python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_health_endpoint():
    """Test the health endpoint"""
    try:
        print("\n🏥 Testing health endpoint...")
        response = requests.get("http://localhost:8000/health", timeout=5)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Health Check Successful!")
            print(f"Status: {result['status']}")
            return True
        else:
            print(f"❌ Health Check Failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Health Check Error: {e}")
        return False

def test_translator_module():
    """Test the core translator module directly"""
    try:
        print("\n🔧 Testing core translator module...")
        from translator import EmojiTranslator
        
        translator = EmojiTranslator()
        
        test_text = "Hello world! I'm feeling great today."
        result = translator.translate(test_text, density="medium", style="fun", add_sentiment=True)
        
        print("✅ Core Translator Test Successful!")
        print(f"📝 Original: {test_text}")
        print(f"🎯 Translated: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Core Translator Test Failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🎯 Emoji Translator AI - System Test")
    print("=" * 60)
    
    # Test core translator
    translator_ok = test_translator_module()
    
    # Test API endpoints
    api_ok = test_api_endpoint()
    health_ok = test_health_endpoint()
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print(f"🔧 Core Translator: {'✅ PASS' if translator_ok else '❌ FAIL'}")
    print(f"🚀 API Endpoint: {'✅ PASS' if api_ok else '❌ FAIL'}")
    print(f"🏥 Health Check: {'✅ PASS' if health_ok else '❌ FAIL'}")
    
    if all([translator_ok, api_ok, health_ok]):
        print("\n🎉 ALL TESTS PASSED! Your Emoji Translator AI is ready to use!")
        print("\n📍 Access your application at:")
        print("   🌐 Web App: http://localhost:8000")
        print("   📖 API Docs: http://localhost:8000/docs")
        print("   🔧 Health Check: http://localhost:8000/health")
    else:
        print("\n⚠️ Some tests failed. Please check the error messages above.")
        print("\n💡 Troubleshooting tips:")
        print("   1. Make sure the server is running: python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload")
        print("   2. Check if port 8000 is available")
        print("   3. Verify all dependencies are installed: pip install fastapi uvicorn[standard] pydantic python-multipart")

if __name__ == "__main__":
    main()
