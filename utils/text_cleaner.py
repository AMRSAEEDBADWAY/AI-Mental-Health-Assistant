"""
Text Cleaner للنصوص العربية واللهجة المصرية
يقوم بتنظيف وتطبيع النص قبل التحليل
"""

import re
import emoji

class ArabicTextCleaner:
    def __init__(self):
        # قاموس تطبيع اللهجة المصرية للفصحى
        self.egyptian_to_standard = {
            'ازاي': 'كيف',
            'ازيك': 'كيف حالك',
            'عامل': 'كيف',
            'ايه': 'ماذا',
            'مش': 'لا',
            'علشان': 'لأن',
            'عشان': 'لأن',
            'لسه': 'لا يزال',
            'خالص': 'جداً',
            'اوي': 'جداً',
            'قوي': 'جداً',
            'برضه': 'أيضاً',
            'كمان': 'أيضاً',
            'بقى': 'أصبح',
            'يعني': 'أي',
            'دلوقتي': 'الآن',
            'حاجة': 'شيء',
            'حاجات': 'أشياء',
            'ناس': 'أشخاص',
            'كده': 'هكذا',
            'كدة': 'هكذا',
            'هو': 'هو',
            'هي': 'هي',
        }
        
        # كلمات دلالية للحالات النفسية باللهجة المصرية
        self.emotion_keywords = {
            'anxiety': ['قلقان', 'خايف', 'متوتر', 'مش مرتاح', 'قلبي مش مطمن', 
                       'خوف', 'توتر', 'قلق', 'مرعوب', 'خايف من المستقبل'],
            'depression': ['زهقان', 'تعبان نفسياً', 'مكتئب', 'مش عايز حاجة', 
                          'حزين', 'مش لاقي معنى', 'مخنوق', 'يئست', 'بكره حياتي', 'زعلان', 'متضايق', 'موجوع'],
            'stress': ['مضغوط', 'مش قادر', 'تحت ضغط', 'مرهق', 'متعب', 
                      'ضغط شديد', 'مش مستحمل', 'كل حاجة صعبة'],
            'happiness': ['فرحان', 'مبسوط', 'سعيد', 'حلو', 'كويس', 
                         'تمام', 'رايق', 'مستمتع'],
            'neutral': ['عادي', 'مش عارف', 'عادي كده', 'طبيعي']
        }
    
    def normalize_arabic(self, text):
        """تطبيع الحروف العربية"""
        # تطبيع الهمزات
        text = re.sub('[إأآا]', 'ا', text)
        # تطبيع الياء
        text = re.sub('ى', 'ي', text)
        # تطبيع التاء المربوطة
        text = re.sub('ة', 'ه', text)
        # إزالة التشكيل
        text = re.sub(r'[\u064B-\u065F]', '', text)
        return text
    
    def remove_emojis(self, text):
        """إزالة الإيموجي من النص"""
        return emoji.replace_emoji(text, replace='')
    
    def clean_text(self, text):
        """تنظيف شامل للنص"""
        # تحويل للأحرف الصغيرة (للإنجليزي)
        text = text.strip()
        
        # إزالة الإيموجي
        text = self.remove_emojis(text)
        
        # إزالة الأرقام الزائدة
        text = re.sub(r'\d+', '', text)
        
        # إزالة الرموز الخاصة (مع الاحتفاظ بعلامات الترقيم الأساسية)
        text = re.sub(r'[^\w\s\u0600-\u06FF.,!?؛،]', '', text)
        
        # تطبيع العربية
        text = self.normalize_arabic(text)
        
        # إزالة المسافات الزائدة
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def map_egyptian_to_standard(self, text):
        """تحويل اللهجة المصرية للفصحى (اختياري)"""
        words = text.split()
        mapped_words = []
        
        for word in words:
            if word in self.egyptian_to_standard:
                mapped_words.append(self.egyptian_to_standard[word])
            else:
                mapped_words.append(word)
        
        return ' '.join(mapped_words)
    
    def detect_emotion_keywords(self, text):
        """الكشف عن الكلمات المفتاحية للمشاعر"""
        text_lower = text.lower()
        detected_emotions = []
        
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    detected_emotions.append(emotion)
                    break
        
        return detected_emotions if detected_emotions else ['neutral']
    
    def preprocess_for_model(self, text, keep_egyptian=True):
        """معالجة كاملة للنص قبل إرساله للنموذج"""
        # تنظيف أساسي
        cleaned = self.clean_text(text)
        
        # اختياري: تحويل للفصحى
        if not keep_egyptian:
            cleaned = self.map_egyptian_to_standard(cleaned)
        
        return cleaned


# دالة مساعدة للاستخدام المباشر
def clean_arabic_text(text, keep_egyptian=True):
    """دالة سريعة لتنظيف النص"""
    cleaner = ArabicTextCleaner()
    return cleaner.preprocess_for_model(text, keep_egyptian)


# اختبار سريع
if __name__ == "__main__":
    cleaner = ArabicTextCleaner()
    
    test_texts = [
        "أنا زهقان قوي النهارده ومش عارف أعمل ايه 😢",
        "حاسس اني قلقان اوي من المستقبل",
        "الحمد لله انا كويس ومبسوط",
    ]
    
    print("=== اختبار Text Cleaner ===\n")
    for text in test_texts:
        cleaned = cleaner.preprocess_for_model(text)
        emotions = cleaner.detect_emotion_keywords(text)
        print(f"النص الأصلي: {text}")
        print(f"بعد التنظيف: {cleaned}")
        print(f"المشاعر المكتشفة: {emotions}\n")