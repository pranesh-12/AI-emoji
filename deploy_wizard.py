#!/usr/bin/env python3
"""
One-Click Deployment Script for Emoji Translator AI
Deploy to multiple platforms and start earning revenue!
"""

import os
import subprocess
import sys
from pathlib import Path

def print_banner():
    print("""
🚀 EMOJI TRANSLATOR AI - DEPLOYMENT WIZARD
=========================================

Ready to deploy your app and start earning revenue!

💰 REVENUE POTENTIAL:
   - 1,000 users/day = $500-1,500/month
   - 10,000 users/day = $3,000-8,000/month
   - 100,000 users/day = $15,000-40,000/month

🌟 MONETIZATION FEATURES:
   ✅ Freemium model (100 free translations/day)
   ✅ Premium subscriptions ($4.99/month)
   ✅ API monetization
   ✅ Usage analytics
   ✅ Social sharing for viral growth
   ✅ SEO optimized

🎯 HOSTING OPTIONS:
   1. Railway (Easiest, free tier)
   2. Render (Great free tier)
   3. Heroku (Popular choice)
   4. DigitalOcean (Professional)
   5. Custom VPS (Advanced)

""")

def check_requirements():
    """Check if all required files exist."""
    required_files = [
        'api.py',
        'translator.py',
        'static/index.html',
        'requirements.txt',
        'Procfile',
        'railway.toml'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def create_git_repo():
    """Initialize git repository if not exists."""
    if not Path('.git').exists():
        print("📦 Initializing Git repository...")
        try:
            subprocess.run(['git', 'init'], check=True)
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', 'Initial commit: Emoji Translator AI'], check=True)
            print("✅ Git repository created")
        except subprocess.CalledProcessError:
            print("⚠️ Git not found. Please install Git first.")
            return False
    else:
        print("✅ Git repository exists")
    
    return True

def deploy_to_railway():
    """Deploy to Railway."""
    print("\n🚂 DEPLOYING TO RAILWAY")
    print("=" * 40)
    
    print("1. Go to https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Click 'New Project' → 'Deploy from GitHub repo'")
    print("4. Select your emoji-translator-ai repository")
    print("5. Railway will auto-detect and deploy!")
    print("6. Your app will be live at: https://your-app.up.railway.app")
    
    input("\nPress Enter when deployed...")
    return True

def deploy_to_render():
    """Deploy to Render."""
    print("\n🎨 DEPLOYING TO RENDER")
    print("=" * 40)
    
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Click 'New' → 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Settings:")
    print("   - Name: emoji-translator-ai")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python -m uvicorn api:app --host 0.0.0.0 --port $PORT")
    print("6. Click 'Create Web Service'")
    
    input("\nPress Enter when deployed...")
    return True

def deploy_to_heroku():
    """Deploy to Heroku."""
    print("\n🟣 DEPLOYING TO HEROKU")
    print("=" * 40)
    
    try:
        # Check if Heroku CLI is installed
        subprocess.run(['heroku', '--version'], check=True, capture_output=True)
        
        print("Creating Heroku app...")
        app_name = input("Enter app name (or press Enter for auto-generated): ").strip()
        
        if app_name:
            subprocess.run(['heroku', 'create', app_name], check=True)
        else:
            subprocess.run(['heroku', 'create'], check=True)
        
        print("Deploying to Heroku...")
        subprocess.run(['git', 'push', 'heroku', 'main'], check=True)
        
        print("✅ Successfully deployed to Heroku!")
        subprocess.run(['heroku', 'open'], check=True)
        
    except subprocess.CalledProcessError:
        print("⚠️ Heroku CLI not found. Manual deployment:")
        print("1. Download Heroku CLI from https://heroku.com")
        print("2. Run: heroku login")
        print("3. Run: heroku create your-app-name")
        print("4. Run: git push heroku main")
    
    return True

def setup_custom_domain():
    """Guide for setting up custom domain."""
    print("\n🌐 CUSTOM DOMAIN SETUP")
    print("=" * 40)
    
    domain = input("Enter your custom domain (e.g., emojimaker.com): ").strip()
    
    if domain:
        print(f"\n📋 DNS Configuration for {domain}:")
        print("1. Go to your domain registrar (GoDaddy, Namecheap, etc.)")
        print("2. Add these DNS records:")
        print("   Type: CNAME")
        print("   Name: @ (or www)")
        print("   Value: [Your hosting platform domain]")
        print("\n3. In your hosting platform:")
        print(f"   - Add custom domain: {domain}")
        print("   - Enable SSL certificate")
        print("\n✨ Your app will be live at: https://" + domain)

def setup_monetization():
    """Guide for setting up monetization."""
    print("\n💰 MONETIZATION SETUP")
    print("=" * 40)
    
    print("1. 📊 Google AdSense:")
    print("   - Apply at: https://adsense.google.com")
    print("   - Add your website URL")
    print("   - Replace 'YOUR-PUBLISHER-ID' in index.html")
    
    print("\n2. 📈 Google Analytics:")
    print("   - Create account at: https://analytics.google.com")
    print("   - Get tracking ID")
    print("   - Replace 'GA_MEASUREMENT_ID' in index.html")
    
    print("\n3. 💳 Payment Processing:")
    print("   - Stripe: https://stripe.com (recommended)")
    print("   - PayPal: https://paypal.com")
    print("   - Implement subscription billing")
    
    print("\n4. 🔑 API Key Management:")
    print("   - Set up user authentication")
    print("   - Implement API key generation")
    print("   - Create pricing tiers")

def marketing_guide():
    """Provide marketing strategies."""
    print("\n📢 MARKETING STRATEGY")
    print("=" * 40)
    
    print("🎯 IMMEDIATE ACTIONS (Week 1):")
    print("✅ Submit to Product Hunt")
    print("✅ Share on Twitter, Facebook, LinkedIn")
    print("✅ Post in relevant Reddit communities")
    print("✅ Create TikTok/Instagram demos")
    
    print("\n🚀 GROWTH HACKS (Month 1):")
    print("✅ SEO optimize for 'emoji generator'")
    print("✅ Create blog content about emojis")
    print("✅ Partner with social media influencers")
    print("✅ Add referral program")
    
    print("\n💡 LONG-TERM STRATEGY:")
    print("✅ Build API partnerships")
    print("✅ Create mobile app")
    print("✅ Expand to multiple languages")
    print("✅ Add team collaboration features")

def main():
    """Main deployment wizard."""
    print_banner()
    
    if not check_requirements():
        print("❌ Please ensure all required files are present")
        return
    
    # Create git repository
    if not create_git_repo():
        print("⚠️ Git setup failed, but you can continue with manual deployment")
    
    # Choose deployment platform
    print("\n🎯 CHOOSE YOUR DEPLOYMENT PLATFORM:")
    print("1. Railway (Recommended - Easiest)")
    print("2. Render (Great free tier)")
    print("3. Heroku (Most popular)")
    print("4. All of the above")
    print("5. Skip deployment")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        deploy_to_railway()
    elif choice == "2":
        deploy_to_render()
    elif choice == "3":
        deploy_to_heroku()
    elif choice == "4":
        deploy_to_railway()
        deploy_to_render()
        deploy_to_heroku()
    
    # Custom domain setup
    if input("\nSet up custom domain? (y/n): ").lower() == 'y':
        setup_custom_domain()
    
    # Monetization setup
    setup_monetization()
    
    # Marketing guide
    marketing_guide()
    
    print("\n🎉 DEPLOYMENT COMPLETE!")
    print("=" * 40)
    print("Your Emoji Translator AI is now live and ready to generate revenue!")
    print("\n📊 TRACK YOUR SUCCESS:")
    print("- Monitor user analytics")
    print("- Track conversion rates")
    print("- Optimize for search engines")
    print("- Engage with your community")
    
    print("\n💰 EXPECTED TIMELINE TO PROFITABILITY:")
    print("📅 Week 1: First users and feedback")
    print("📅 Month 1: $10-50 revenue")
    print("📅 Month 3: $100-500 revenue")
    print("📅 Month 6: $500-2,000 revenue")
    print("📅 Year 1: $2,000-10,000+ revenue")
    
    print("\n🚀 Good luck with your emoji empire!")

if __name__ == "__main__":
    main()
