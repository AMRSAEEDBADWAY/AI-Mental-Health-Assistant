import streamlit as st

# إعداد الصفحة - يجب أن يكون أول شيء
st.set_page_config(
    page_title="AI Mental Health Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

from emotion_model import EmotionDetector
from response_generator import GeminiResponseGenerator
from mood_tracker import MoodTracker, display_mood_analytics
from therapy_exercises import display_therapy_exercises, TherapyExercises
from ui_components import UIComponents, create_welcome_animation
from resources_library import display_resources_library, display_daily_tip, ResourcesLibrary

def initialize_session_state():
    """تهيئة الذاكرة"""
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'المحادثة'
    if 'show_welcome' not in st.session_state:
        st.session_state.show_welcome = True

def main():
    """الدالة الرئيسية للتطبيق"""
    # تهيئة الذاكرة
    initialize_session_state()
    
    # إنشاء كائنات النماذج والمكونات
    emotion_model = EmotionDetector()
    response_gen = GeminiResponseGenerator()
    mood_tracker = MoodTracker()
    therapy_exercises = TherapyExercises()
    ui_components = UIComponents()
    resources_library = ResourcesLibrary()
    
    # Sidebar - القائمة الجانبية المحسنة
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; color: white; margin-bottom: 1rem;'>
            <h2>🧠 مساعدك النفسي الذكي</h2>
            <p>نحن هنا لدعمك دائماً</p>
        </div>
        """, unsafe_allow_html=True)
        
        # قائمة التنقل
        st.subheader("📋 القوائم")
        pages = {
            "💬 المحادثة": "المحادثة",
            "📊 التحليلات": "التحليلات", 
            "🧘 التمارين": "التمارين",
            "📚 المكتبة": "المكتبة",
            "⚙️ الإعدادات": "الإعدادات"
        }
        
        for page_name, page_key in pages.items():
            if st.button(page_name, key=f"nav_{page_key}", use_container_width=True):
                st.session_state.current_page = page_key
                st.rerun()
        
        st.markdown("---")
        
        # نصيحة اليوم في الشريط الجانبي
        daily_tip = resources_library.get_daily_tip()
        st.markdown(f"""
        <div style='background: #4CAF50; padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h4>{daily_tip['icon']} نصيحة اليوم</h4>
            <p style='font-size: 0.9rem; margin: 0;'>{daily_tip['tip']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # معلومات سريعة
        st.markdown("""
        ### ℹ️ معلومات مهمة
        
        **هذا المساعد:**
        - ✅ يقدم دعماً نفسياً أولياً
        - ✅ يساعدك على فهم مشاعرك
        - ✅ يوفر تمارين وتقنيات مفيدة
        
        **ليس بديلاً عن:**
        - ❌ الطبيب النفسي المتخصص
        - ❌ التشخيص الطبي
        - ❌ وصف الأدوية
        
        **في حالات الطوارئ:**
        📞 اتصل بـ 08008880700
        """)
        
        if st.button("🔄 بدء محادثة جديدة", use_container_width=True):
            st.session_state.conversation_history = []
            st.session_state.messages = []
            st.session_state.show_welcome = True
            st.rerun()

    # عرض الصفحة المحددة
    if st.session_state.current_page == "المحادثة":
        # العنوان الرئيسي مع تصميم محسن
        ui_components.create_gradient_title(
            "🧠 الطبيب النفسي الذكي", 
            "محادثة سرية وآمنة مع مساعدك الذكي 💚"
        )
        
        # رسالة ترحيبية متحركة للمستخدمين الجدد
        if st.session_state.show_welcome and len(st.session_state.messages) == 0:
            create_welcome_animation()
            st.session_state.show_welcome = False

        # عرض الرسائل السابقة
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "emotion" in message:
                    st.caption(f"🎭 الحالة: {message['emotion']}")

        # صندوق الإدخال
        if prompt := st.chat_input("اكتب هنا... أنا موجود للاستماع لك 💙"):
            
            # عرض رسالة المستخدم
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # تحليل المشاعر مع واجهة محسنة
            with st.spinner("🔍 بحلل كلامك..."):
                emotion_result = emotion_model.detect_emotion(prompt)
                emotion = emotion_result["emotion"]
                confidence = emotion_result["confidence"]
                description = emotion_result["description_ar"]
            
            # عرض نتيجة التحليل بتصميم جميل
            ui_components.create_mood_card(emotion, confidence, description)
            
            # توليد الرد من النظام الذكي
            with st.spinner("💭 بفكر في الرد المناسب..."):
                # تحضير تاريخ المحادثة
                history_text = ""
                for conv in st.session_state.conversation_history[-3:]:  # آخر 3 محادثات
                    history_text += f"المستخدم: {conv['user']}\nالمساعد: {conv['assistant']}\n"
                
                ai_response = response_gen.generate_ai_response(
                    user_text=prompt,
                    emotion=emotion,
                    history=history_text
                )
            
            # حفظ في نظام تتبع المزاج
            mood_tracker.add_mood_entry(emotion, confidence, prompt, ai_response)
            
            # اقتراح تمرين مناسب
            recommended_exercise = therapy_exercises.get_recommended_exercise(emotion)
            if recommended_exercise:
                st.info(f"💡 **اقتراح:** جرب تمرين '{recommended_exercise['exercise']}' - {recommended_exercise['reason']}")
            
            # حفظ في الذاكرة
            st.session_state.conversation_history.append({
                "user": prompt,
                "emotion": emotion,
                "assistant": ai_response
            })
            
            if len(st.session_state.conversation_history) > 10:
                st.session_state.conversation_history = st.session_state.conversation_history[-10:]
            
            # إضافة رد المساعد
            st.session_state.messages.append({
                "role": "assistant",
                "content": ai_response,
                "emotion": emotion
            })
            
            # عرض الرد
            with st.chat_message("assistant"):
                st.markdown(ai_response)
                st.caption(f"🎭 الحالة المكتشفة: {emotion}")

        # رسالة ترحيبية محسنة
        if len(st.session_state.messages) == 0:
            ui_components.create_custom_alert(
                "أهلاً وسهلاً! أنا هنا لأسمعك وأساعدك. احكيلي عن أي شيء في بالك - كل كلامنا سري وآمن 💚",
                "info", "👋"
            )
            
            # عرض مميزات التطبيق
            features = [
                {"icon": "🎭", "title": "تحليل المشاعر", "description": "فهم حالتك النفسية"},
                {"icon": "🧘", "title": "تمارين مفيدة", "description": "تقنيات الاسترخاء"},
                {"icon": "📊", "title": "تتبع التقدم", "description": "رسوم بيانية للمزاج"},
                {"icon": "📚", "title": "مكتبة الموارد", "description": "نصائح ومقالات"}
            ]
            ui_components.create_feature_grid(features)

    elif st.session_state.current_page == "التحليلات":
        display_mood_analytics()

    elif st.session_state.current_page == "التمارين":
        display_therapy_exercises()

    elif st.session_state.current_page == "المكتبة":
        display_resources_library()

    elif st.session_state.current_page == "الإعدادات":
        st.header("⚙️ الإعدادات")
        
        st.subheader("🎨 تخصيص الواجهة")
        
        # خيارات الواجهة
        col1, col2 = st.columns(2)
        
        with col1:
            dark_mode = st.checkbox("🌙 الوضع الليلي", key="dark_mode")
            if dark_mode:
                st.info("سيتم تطبيق الوضع الليلي قريباً")
        
        with col2:
            notifications = st.checkbox("🔔 التنبيهات", value=True, key="notifications")
        
        st.subheader("📊 إعدادات البيانات")
        
        if st.button("🗑️ مسح جميع البيانات", type="secondary"):
            if st.checkbox("أؤكد رغبتي في مسح جميع البيانات"):
                st.session_state.conversation_history = []
                st.session_state.messages = []
                # يمكن إضافة مسح بيانات المزاج هنا
                st.success("تم مسح البيانات بنجاح!")
                st.rerun()
        
        st.subheader("ℹ️ معلومات التطبيق")
        st.info("""
        **الإصدار:** 2.0.0
        **آخر تحديث:** نوفمبر 2024
        **المطور:** فريق الصحة النفسية الذكية
        
        **المميزات الجديدة:**
        - 📊 تتبع الحالة المزاجية
        - 🧘 تمارين تفاعلية
        - 📚 مكتبة موارد شاملة
        - 🎨 واجهة محسنة
        """)

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #888;'>"
        "Made with ❤️ using Google Gemini AI | "
        "لا تتردد في طلب المساعدة المتخصصة عند الحاجة"
        "</div>",
        unsafe_allow_html=True
    )

# تشغيل التطبيق
if __name__ == "__main__":
    main()
