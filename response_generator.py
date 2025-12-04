"""
مولد الردود الذكية باستخدام Gemini API المجاني
يدعم اللهجة المصرية والدعم النفسي المتقدم (شخصية د. أمل)
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# تحميل مفتاح Gemini API
load_dotenv()

api_key = None

# محاولة قراءة من Streamlit Secrets (فقط إذا كان الملف موجوداً لتجنب التحذيرات)
try:
    # التحقق من وجود ملف secrets.toml لتجنب تحذير Streamlit
    secrets_path = os.path.join(".streamlit", "secrets.toml")
    if os.path.exists(secrets_path):
        if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

# إذا لم يتم العثور على المفتاح في Secrets، جرب .env
if not api_key:
    api_key = os.getenv("GEMINI_API_KEY")

# رسالة خطأ واضحة مع تعليمات
if not api_key or api_key == "your-gemini-api-key-here":
    error_msg = """
    ❌ لم يتم العثور على مفتاح Gemini API!
    """
    # لا نرفع الخطأ هنا لتجنب توقف التطبيق بالكامل، بل نتركه يفشل عند الاستخدام
    print(error_msg)
else:
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring Gemini: {e}")

class GeminiResponseGenerator:
    def __init__(self):
        print("Gemini initialized successfully!")
        self.system_prompt = """
        أنتِ "د. أمل"، طبيبة نفسية مصرية محترفة ومتعاطفة جداً.
        دورك هو تقديم الدعم النفسي الأولي، الاستماع الفعال، والمساعدة في ترتيب الأفكار.
        
        صفات شخصيتك:
        1. **متعاطفة جداً**: تشعرين بألم المستخدم وتظهرين ذلك في كلامك ("أنا حاسة بيك"، "حقك تتضايق").
        2. **مصرية أصيلة**: تتكلمين باللهجة المصرية الدافئة والبسيطة (مش فصحى معقدة ولا عامية سوقية).
        3. **محترفة**: لا تحكمين على المستخدم، ولا تقدمين تشخيصات طبية قاطعة، ولا تصفين أدوية.
        4. **إيجابية وواقعية**: تركزين على الحلول الصغيرة الممكنة (Baby Steps).
        
        طريقة ردك (CBT Approach):
        1. **Validation (التقبل)**: ابدأي دائماً بتقبل مشاعر المستخدم وتأكيد أنها طبيعية.
        2. **Exploration (الاستكشاف)**: اسألي أسئلة مفتوحة لفهم الأفكار وراء المشاعر.
        3. **Reframing (إعادة الصياغة)**: ساعدي المستخدم يشوف الموضوع من زاوية تانية بأسلوب لطيف.
        4. **Action (العمل)**: اقترحي خطوة صغيرة جداً وعملية يقدر يعملها دلوقتي.
        
        قواعد صارمة:
        - لا تتجاوزي 5-6 أسطر في الرد الواحد (خليكي مركزة).
        - دائماً انهي الرد بسؤال متابعة يشجع المستخدم يكمل كلام.
        - لو المستخدم لمح للانتحار أو إيذاء النفس، وجهيه فوراً للخط الساخن (08008880700) بلطف وحزم.
        """

    def generate_ai_response(self, user_text, emotion, history):
        """
        توليد رد ذكي باستخدام Gemini
        """
        
        # بناء السياق الكامل
        full_prompt = f"""
        {self.system_prompt}
        
        سياق المحادثة الحالية:
        {history}
        
        معلومات إضافية عن الحالة الآن:
        - مشاعر المستخدم المكتشفة: {emotion}
        - رسالة المستخدم الأخيرة: {user_text}
        
        المطلوب:
        ردي على المستخدم بصفتك "د. أمل" بناءً على القواعد السابقة.
        """

        try:
            # استخدام أحدث نموذج متاح
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(full_prompt)
            return response.text.strip()

        except Exception as e:
            print(f"Gemini Error: {e}")
            # في حالة فشل Gemini، استخدم رد افتراضي ذكي
            return self.generate_fallback_response(user_text, emotion)

    def generate_fallback_response(self, user_text, emotion):
        """رد احتياطي في حالة فشل Gemini"""
        responses = {
            'anxiety': [
                "أنا حاسة بقلقك، وده شعور طبيعي لما نكون مضغوطين. خدي نفس عميق معايا.. شهيق.. زفير. إيه أكتر فكرة مسيطرة عليك دلوقتي؟",
                "القلق عامل زي الدوشة في الدماغ، بيخلينا مش عارفين نركز. تعالي نحاول نرتب الأفكار دي سوا. إيه اللي مخوفك تحديداً؟"
            ],
            'depression': [
                "أنا مقدرة جداً الألم اللي حاسس بيه. الأيام الصعبة دي بتعدي، حتى لو حاسس إنها مش هتخلص. أنا هنا جنبك وسامعاك. حابب تحكيلي أكتر عن اللي مضايقك؟",
                "حقك تكون زعلان، ومفيش داعي تضغط على نفسك عشان تكون 'كويس' دلوقتي. سيب مشاعرك تطلع. إيه اللي شاغل بالك؟"
            ],
            'stress': [
                "واضح إن الحمل تقيل عليك الفترة دي. بس صدقني، كل مشكلة وليها حل لما تتقسم لأجزاء صغيرة. إيه أول حاجة ممكن نخلصها عشان نخفف الضغط ده؟",
                "الضغط النفسي بيسحب طاقتنا، عشان كده مهم نكون رحيمين بنفسنا. إيه رأيك ناخد بريك صغير ونفكر سوا في حل؟"
            ],
            'happiness': [
                "يا سلام! الأخبار الحلوة دي بتفرحني جداً. يارب دايماً مبسوط. إيه اللي خلاك تحس بالسعادة دي النهارده؟",
                "طاقتك الإيجابية وصلتلي! جميل إننا نقدر اللحظات الحلوة دي. احكيلي أكتر، إيه اللي حصل؟"
            ],
            'neutral': [
                "أهلاً بيك يا بطل. أنا د. أمل، موجودة هنا عشان أسمعك في أي وقت. يومك كان عامل إزاي؟",
                "أنا سامعاك ومهتمة أعرف أخبارك. في حاجة معينة شاغلة تفكيرك النهارده؟"
            ]
        }
        
        import random
        emotion_responses = responses.get(emotion, responses['neutral'])
        return random.choice(emotion_responses)

    def generate_followup_question(self, emotion):
        """سؤال متابعة مناسب للحالة"""
        followups = {
            'anxiety': "إيه أسوأ سيناريو خايف منه؟ وهل هو واقعي؟",
            'depression': "إيه الحاجة الصغيرة اللي لو حصلت دلوقتي ممكن تحسن مزاجك ولو 1%؟",
            'stress': "مين ممكن يساعدك تشيل الحمل ده معاك؟",
            'happiness': "إزاي ممكن نحافظ على الشعور الجميل ده لبكرة؟",
            'neutral': "إيه اللي نفسك تحققه الفترة الجاية؟"
        }
        return followups.get(emotion, "تحب نتكلم في إيه كمان؟")

# اختبار سريع
if __name__ == "__main__":
    model = GeminiResponseGenerator()
    history = "المستخدم: أنا قلقان.\nالمساعد: أفهمك، إيه اللي مسببلك القلق؟"
    print(model.generate_ai_response("حاسس إن الامتحانات قربت ومتوتر", "anxiety", history))
