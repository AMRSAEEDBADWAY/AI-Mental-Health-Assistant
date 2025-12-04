#!/usr/bin/env python3
"""
ملف تشغيل سريع للتطبيق
يتحقق من المتطلبات ويشغل التطبيق
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """فحص إصدار Python"""
    if sys.version_info < (3, 8):
        print("❌ يتطلب Python 3.8 أو أحدث")
        print(f"الإصدار الحالي: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True

def check_requirements():
    """فحص المكتبات المطلوبة"""
    required_packages = [
        'streamlit',
        'pandas', 
        'numpy',
        'google-generativeai',
        'python-dotenv',
        'emoji'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} غير مثبت")
    
    return missing_packages

def install_requirements():
    """تثبيت المتطلبات"""
    print("🔄 جاري تثبيت المكتبات المطلوبة...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ تم تثبيت جميع المكتبات بنجاح!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ فشل في تثبيت المكتبات: {e}")
        return False

def check_env_file():
    """فحص ملف البيئة"""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("⚠️ ملف .env غير موجود")
        
        # إنشاء ملف .env من النموذج
        template_file = Path(".env.example")
        if template_file.exists():
            try:
                import shutil
                shutil.copy(template_file, env_file)
                print("✅ تم إنشاء ملف .env من النموذج")
            except Exception as e:
                print(f"❌ فشل في إنشاء ملف .env: {e}")
                return False
        else:
            print("❌ ملف النموذج .env.example غير موجود")
            return False
    else:
        print("✅ ملف .env موجود")
    
    return True

def create_data_directories():
    """إنشاء مجلدات البيانات"""
    directories = ["data", "models", "logs"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ مجلد {directory}")

def run_app():
    """تشغيل التطبيق"""
    print("\nStarting the application...")
    print("Note: The app will open in your browser automatically")
    print("URL: http://localhost:8501")
    print("To stop: Press Ctrl+C\n")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.address", "localhost",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\nApp stopped successfully!")
    except Exception as e:
        print(f"\nError running app: {e}")

def main():
    """الدالة الرئيسية"""
    print("AI Mental Health Assistant - Version 2.0")
    print("=" * 50)
    
    # فحص إصدار Python
    if not check_python_version():
        return
    
    # فحص المكتبات
    missing = check_requirements()
    
    if missing:
        print(f"\nMissing packages: {', '.join(missing)}")
        
        install_choice = input("Do you want to install them now? (y/n): ").lower().strip()
        
        if install_choice in ['y', 'yes']:
            if not install_requirements():
                print("Installation failed. Please install manually:")
                print("pip install -r requirements.txt")
                return
        else:
            print("Cannot run the app without required packages")
            return
    
    # فحص ملف البيئة
    if not check_env_file():
        print("Check Gemini API settings in .env file")
    
    # إنشاء المجلدات
    create_data_directories()
    
    print("\nAll requirements ready!")
    
    # تشغيل التطبيق
    run_choice = input("\nDo you want to run the app now? (y/n): ").lower().strip()
    
    if run_choice in ['y', 'yes']:
        run_app()
    else:
        print("You can run the app later using:")
        print("python run.py")
        print("or")
        print("streamlit run app.py")

if __name__ == "__main__":
    main()


