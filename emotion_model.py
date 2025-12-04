"""
نموذج تحليل المشاعر باستخدام MARBERT
يدعم النصوص العربية واللهجة المصرية
"""

# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers import pipeline
# import numpy as np
from utils.text_cleaner import ArabicTextCleaner

class EmotionDetector:
    def __init__(self, model_name="CAMeL-Lab/bert-base-arabic-camelbert-msa-sentiment"):
        """
        تهيئة نموذج MARBERT لتحليل المشاعر
        
        Args:
            model_name: اسم النموذج من HuggingFace
        """
        print("Loading emotion analysis system...")
        
        # استخدام التحليل القائم على الكلمات المفتاحية فقط للبساطة
        print("Using keyword-based analysis")
        self.sentiment_pipeline = None
        
        # يمكن تفعيل النموذج لاحقاً إذا أردت
        # try:
        #     # تحميل النموذج والـ Tokenizer
        #     self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        #     self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        #     
        #     # إنشاء Pipeline
        #     self.sentiment_pipeline = pipeline(
        #         "sentiment-analysis",
        #         model=self.model,
        #         tokenizer=self.tokenizer,
        #         device=-1  # CPU only (-1), for GPU use 0
        #     )
        #     
        #     print("✅ تم تحميل النموذج بنجاح!")
        #     
        # except Exception as e:
        #     print(f"❌ خطأ في تحميل النموذج: {e}")
        #     print("📌 سيتم استخدام التحليل القائم على الكلمات المفتاحية")
        #     self.sentiment_pipeline = None
        
        # تهيئة منظف النصوص
        self.text_cleaner = ArabicTextCleaner()
        
        # قاموس تحويل المشاعر
        self.emotion_mapping = {
            'positive': 'happiness',
            'negative': 'depression',
            'neutral': 'neutral',
            'POSITIVE': 'happiness',
            'NEGATIVE': 'depression',
            'NEUTRAL': 'neutral'
        }
        
        # أوزان المشاعر حسب الكلمات المفتاحية
        self.emotion_scores = {
            'anxiety': 0,
            'depression': 0,
            'stress': 0,
            'happiness': 0,
            'neutral': 0
        }
    
    def analyze_with_keywords(self, text):
        """تحليل باستخدام الكلمات المفتاحية (Fallback Method)"""
        keywords_found = self.text_cleaner.detect_emotion_keywords(text)
        
        # حساب النتيجة
        scores = self.emotion_scores.copy()
        for emotion in keywords_found:
            if emotion in scores:
                scores[emotion] += 1
        
        # إيجاد أعلى نتيجة
        if sum(scores.values()) == 0:
            return 'neutral', 0.5
        
        max_emotion = max(scores, key=scores.get)
        confidence = scores[max_emotion] / sum(scores.values())
        
        return max_emotion, confidence
    
    def analyze_with_model(self, text):
        """تحليل باستخدام نموذج MARBERT"""
        try:
            result = self.sentiment_pipeline(text)[0]
            sentiment_label = result['label']
            confidence = result['score']
            
            # تحويل للمشاعر المطلوبة
            emotion = self.emotion_mapping.get(sentiment_label, 'neutral')
            
            # تحسين التصنيف بناءً على الكلمات المفتاحية
            keyword_emotions = self.text_cleaner.detect_emotion_keywords(text)
            
            if 'anxiety' in keyword_emotions and emotion == 'depression':
                emotion = 'anxiety'
            elif 'stress' in keyword_emotions:
                emotion = 'stress'
            
            return emotion, confidence
            
        except Exception as e:
            print(f"⚠️ تحذير: {e}")
            return self.analyze_with_keywords(text)
    
    def detect_emotion(self, text, use_model=True):
        """
        الدالة الرئيسية لتحليل المشاعر
        
        Args:
            text: النص المراد تحليله
            use_model: استخدام النموذج أم الكلمات المفتاحية فقط
            
        Returns:
            dict: {
                'emotion': الحالة النفسية,
                'confidence': نسبة الثقة,
                'description_ar': وصف بالعربية
            }
        """
        # تنظيف النص
        cleaned_text = self.text_cleaner.preprocess_for_model(text)
        
        if len(cleaned_text) < 3:
            return {
                'emotion': 'neutral',
                'confidence': 0.5,
                'description_ar': 'نص قصير جداً'
            }
        
        # تحليل المشاعر
        if use_model and self.sentiment_pipeline:
            emotion, confidence = self.analyze_with_model(cleaned_text)
        else:
            emotion, confidence = self.analyze_with_keywords(cleaned_text)
        
        # إضافة وصف عربي
        descriptions = {
            'anxiety': 'حالة قلق وتوتر',
            'depression': 'حالة حزن واكتئاب',
            'stress': 'حالة ضغط نفسي',
            'happiness': 'حالة سعادة وراحة',
            'neutral': 'حالة طبيعية'
        }
        
        return {
            'emotion': emotion,
            'confidence': round(confidence, 2),
            'description_ar': descriptions.get(emotion, 'غير محدد'),
            'source': 'MARBERT AI' if (use_model and self.sentiment_pipeline) else 'Keyword Analysis'
        }
    
    def get_emotion_emoji(self, emotion):
        """الحصول على إيموجي للحالة"""
        emojis = {
            'anxiety': '😰',
            'depression': '😢',
            'stress': '😫',
            'happiness': '😊',
            'neutral': '😐'
        }
        return emojis.get(emotion, '🙂')


# دالة مساعدة للاستخدام السريع
def quick_emotion_check(text):
    """فحص سريع للمشاعر"""
    detector = EmotionDetector()
    return detector.detect_emotion(text)


# اختبار النموذج
if __name__ == "__main__":
    print("=== اختبار نموذج تحليل المشاعر ===\n")
    
    detector = EmotionDetector()
    
    test_cases = [
        "أنا زهقان قوي ومش عايز أعمل حاجة",
        "قلقان من الامتحانات اوي",
        "الحمد لله انا كويس ومبسوط",
        "الشغل كتير اوي ومش قادر استحمل الضغط ده",
        "النهارده يوم جميل"
    ]
    
    for text in test_cases:
        result = detector.detect_emotion(text)
        emoji = detector.get_emotion_emoji(result['emotion'])
        
        print(f"📝 النص: {text}")
        print(f"{emoji} الحالة: {result['emotion']}")
        print(f"📊 الثقة: {result['confidence']*100:.1f}%")
        print(f"📋 الوصف: {result['description_ar']}\n")