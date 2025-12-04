"""
ملف التكوين الرئيسي للتطبيق
يحتوي على جميع الإعدادات والثوابت
"""

import os
from pathlib import Path

class Config:
    """كلاس التكوين الرئيسي"""
    
    # إعدادات التطبيق الأساسية
    APP_NAME = "AI Mental Health Assistant"
    APP_VERSION = "2.0.0"
    APP_DESCRIPTION = "مساعد الصحة النفسية الذكي - يدعم اللهجة المصرية"
    
    # مسارات الملفات
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    MODELS_DIR = BASE_DIR / "models"
    LOGS_DIR = BASE_DIR / "logs"
    
    # إنشاء المجلدات إذا لم تكن موجودة
    DATA_DIR.mkdir(exist_ok=True)
    MODELS_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)
    
    # ملفات البيانات
    MOOD_HISTORY_FILE = DATA_DIR / "mood_history.json"
    EXERCISE_PROGRESS_FILE = DATA_DIR / "exercise_progress.json"
    USER_PREFERENCES_FILE = DATA_DIR / "user_preferences.json"
    CONVERSATION_BACKUP_FILE = DATA_DIR / "conversation_backup.json"
    
    # إعدادات النماذج
    DEFAULT_EMOTION_MODEL = "CAMeL-Lab/bert-base-arabic-camelbert-msa-sentiment"
    GEMINI_MODEL_NAME = "gemini-2.5-flash"
    MAX_CONVERSATION_HISTORY = 10
    
    # إعدادات واجهة المستخدم
    UI_THEME = {
        "primary_color": "#4CAF50",
        "secondary_color": "#2196F3", 
        "accent_color": "#FF9800",
        "success_color": "#8BC34A",
        "warning_color": "#FFC107",
        "error_color": "#F44336",
        "background_gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    }
    
    # إعدادات التحليلات
    ANALYTICS_SETTINGS = {
        "default_analysis_period": 30,  # أيام
        "min_entries_for_analysis": 5,
        "confidence_threshold": 0.7,
        "chart_colors": {
            'happiness': '#2E8B57',
            'neutral': '#4682B4',
            'anxiety': '#FF6347',
            'stress': '#FF4500',
            'depression': '#8B0000'
        }
    }
    
    # إعدادات التمارين
    EXERCISE_SETTINGS = {
        "breathing_default_duration": 5,  # دقائق
        "mindfulness_default_duration": 10,  # دقائق
        "daily_challenge_reset_hour": 6,  # الساعة 6 صباحاً
        "exercise_reminder_interval": 4  # كل 4 ساعات
    }
    
    # إعدادات الأمان والخصوصية
    PRIVACY_SETTINGS = {
        "data_retention_days": 365,  # سنة واحدة
        "auto_backup_enabled": True,
        "encryption_enabled": False,  # للمستقبل
        "anonymous_analytics": True
    }
    
    # رسائل النظام
    SYSTEM_MESSAGES = {
        "welcome": "مرحباً بك في مساعدك النفسي الذكي! 🧠",
        "error_general": "حدث خطأ غير متوقع. يرجى المحاولة مرة أخرى.",
        "error_model": "عذراً، لا يمكن تحليل النص حالياً. جرب مرة أخرى.",
        "error_api": "مشكلة في الاتصال بالخدمة. تحقق من الإنترنت.",
        "data_saved": "تم حفظ بياناتك بنجاح! ✅",
        "exercise_completed": "أحسنت! أكملت التمرين بنجاح! 🎉"
    }
    
    # جهات الاتصال الطارئة
    EMERGENCY_CONTACTS = {
        "egypt": {
            "mental_health_hotline": "08008880700",
            "emergency": "123",
            "abbasia_hospital": "0227940000"
        },
        "international": {
            "suicide_prevention": "https://www.iasp.info/resources/Crisis_Centres/"
        }
    }
    
    # إعدادات التطوير
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # إعدادات الأداء
    PERFORMANCE_SETTINGS = {
        "cache_enabled": True,
        "max_cache_size": 100,  # MB
        "session_timeout": 3600,  # ثانية (ساعة واحدة)
        "max_file_size": 10  # MB للتحميلات
    }
    
    @classmethod
    def get_env_var(cls, key, default=None):
        """الحصول على متغير بيئة مع قيمة افتراضية"""
        return os.getenv(key, default)
    
    @classmethod
    def is_production(cls):
        """فحص ما إذا كان التطبيق في بيئة الإنتاج"""
        return cls.get_env_var("ENVIRONMENT", "development") == "production"
    
    @classmethod
    def get_database_url(cls):
        """الحصول على رابط قاعدة البيانات (للمستقبل)"""
        return cls.get_env_var("DATABASE_URL", "sqlite:///mental_health.db")


class UIConfig:
    """إعدادات واجهة المستخدم"""
    
    # الألوان والتصميم
    COLORS = Config.UI_THEME
    
    # الخطوط
    FONTS = {
        "primary": "Cairo, sans-serif",
        "secondary": "Arial, sans-serif",
        "monospace": "Courier New, monospace"
    }
    
    # أحجام الخط
    FONT_SIZES = {
        "small": "0.8rem",
        "normal": "1rem", 
        "medium": "1.2rem",
        "large": "1.5rem",
        "xlarge": "2rem"
    }
    
    # المسافات
    SPACING = {
        "xs": "0.25rem",
        "sm": "0.5rem",
        "md": "1rem",
        "lg": "1.5rem",
        "xl": "2rem",
        "xxl": "3rem"
    }
    
    # نقاط الانكسار للتصميم المتجاوب
    BREAKPOINTS = {
        "mobile": "768px",
        "tablet": "1024px", 
        "desktop": "1200px"
    }


class AnalyticsConfig:
    """إعدادات التحليلات والإحصائيات"""
    
    # فترات التحليل المتاحة
    ANALYSIS_PERIODS = [7, 14, 30, 60, 90, 180, 365]
    
    # أنواع الرسوم البيانية
    CHART_TYPES = {
        "line": "خط بياني",
        "bar": "أعمدة بيانية", 
        "pie": "دائري",
        "area": "منطقة",
        "scatter": "نقطي"
    }
    
    # مقاييس الأداء
    METRICS = {
        "mood_average": "متوسط المزاج",
        "mood_trend": "اتجاه المزاج",
        "exercise_completion": "إكمال التمارين",
        "session_frequency": "تكرار الجلسات",
        "improvement_rate": "معدل التحسن"
    }


class ExerciseConfig:
    """إعدادات التمارين والتقنيات"""
    
    # أنواع التمارين
    EXERCISE_TYPES = {
        "breathing": "تمارين التنفس",
        "mindfulness": "اليقظة الذهنية",
        "cognitive": "التمارين المعرفية",
        "gratitude": "تمارين الامتنان",
        "relaxation": "تمارين الاسترخاء"
    }
    
    # مستويات الصعوبة
    DIFFICULTY_LEVELS = {
        "beginner": "مبتدئ",
        "intermediate": "متوسط", 
        "advanced": "متقدم"
    }
    
    # أوقات التمارين الافتراضية (بالدقائق)
    DEFAULT_DURATIONS = {
        "breathing": 5,
        "mindfulness": 10,
        "cognitive": 15,
        "gratitude": 5,
        "relaxation": 20
    }


# تصدير الإعدادات للاستخدام السهل
config = Config()
ui_config = UIConfig()
analytics_config = AnalyticsConfig()
exercise_config = ExerciseConfig()

# دالة مساعدة للحصول على الإعدادات
def get_config(section=None):
    """الحصول على إعدادات معينة أو جميع الإعدادات"""
    if section == "ui":
        return ui_config
    elif section == "analytics":
        return analytics_config
    elif section == "exercise":
        return exercise_config
    else:
        return config


if __name__ == "__main__":
    # اختبار الإعدادات
    print(f"اسم التطبيق: {config.APP_NAME}")
    print(f"الإصدار: {config.APP_VERSION}")
    print(f"مجلد البيانات: {config.DATA_DIR}")
    print(f"وضع التطوير: {config.DEBUG}")
    print(f"بيئة الإنتاج: {config.is_production()}")
    
    # اختبار إنشاء المجلدات
    print(f"مجلد البيانات موجود: {config.DATA_DIR.exists()}")
    print(f"مجلد النماذج موجود: {config.MODELS_DIR.exists()}")
    
    print("تم تحميل الإعدادات بنجاح! ✅")


