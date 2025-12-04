import streamlit as st

# إعداد الصفحة - يجب أن يكون أول شيء
st.set_page_config(
    page_title="AI Mental Health Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = True  # الوضع الليلي افتراضي
    if 'models_loaded' not in st.session_state:
        st.session_state.models_loaded = {}

@st.cache_resource(ttl=3600)  # Cache لمدة ساعة
def load_emotion_model_v2():
    """تحميل نموذج المشاعر مع Cache - V2"""
    from emotion_model import EmotionDetector
    return EmotionDetector()

@st.cache_resource(ttl=3600)
def load_response_model():
    """تحميل نموذج الردود مع Cache"""
    from response_generator import GeminiResponseGenerator
    return GeminiResponseGenerator()

@st.cache_resource(ttl=3600)
def load_tracker():
    """تحميل نظام التتبع مع Cache"""
    from mood_tracker import MoodTracker
    return MoodTracker()

@st.cache_resource(ttl=3600)
def load_exercises():
    """تحميل التمارين مع Cache"""
    from therapy_exercises import TherapyExercises
    return TherapyExercises()

@st.cache_resource(ttl=3600)
def load_resources():
    """تحميل الموارد مع Cache"""
    from resources_library import ResourcesLibrary
    return ResourcesLibrary()

@st.cache_resource(ttl=3600)
def load_ui():
    """تحميل مكونات الواجهة مع Cache"""
    from ui_components import UIComponents
    return UIComponents()

def load_model(model_name):
    """تحميل النماذج عند الحاجة فقط (Lazy Loading) مع Cache"""
    if model_name not in st.session_state.models_loaded:
        if model_name == 'emotion':
            st.session_state.models_loaded[model_name] = load_emotion_model_v2()
        elif model_name == 'response':
            st.session_state.models_loaded[model_name] = load_response_model()
        elif model_name == 'tracker':
            st.session_state.models_loaded[model_name] = load_tracker()
        elif model_name == 'exercises':
            st.session_state.models_loaded[model_name] = load_exercises()
        elif model_name == 'resources':
            st.session_state.models_loaded[model_name] = load_resources()
        elif model_name == 'ui':
            st.session_state.models_loaded[model_name] = load_ui()
    
    return st.session_state.models_loaded.get(model_name)

def main():
    """الدالة الرئيسية للتطبيق"""
    # تهيئة الذاكرة
    initialize_session_state()
    
    # تحسين سرعة التنقل - تعطيل بعض الميزات الثقيلة
    st.markdown("""
    <style>
    /* تعطيل التحريكات الثقيلة */
    .fade-in {
        animation: none !important;
    }
    
    /* تحسين سرعة التمرير */
    html {
        scroll-behavior: smooth;
    }
    
    /* تحسين الأداء العام */
    .element-container {
        will-change: auto;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar - القائمة الجانبية المحسنة
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; color: white; margin-bottom: 1rem;'>
            <h2>🧠 مساعدك النفسي الذكي</h2>
            <p>نحن هنا لدعمك دائماً</p>
        </div>
        """, unsafe_allow_html=True)
        
        # قائمة التنقل السريع
        st.subheader("📋 القوائم")
        pages = {
            "💬 المحادثة": "المحادثة",
            "📊 التحليلات": "التحليلات", 
            "🧘 التمارين": "التمارين",
            "📚 المكتبة": "المكتبة",
            "⚙️ الإعدادات": "الإعدادات"
        }
        
        # أزرار تنقل سريعة - تحسين للأداء
        cols = st.columns(2)
        for idx, (page_name, page_key) in enumerate(pages.items()):
            with cols[idx % 2]:
                # تمييز الصفحة النشطة
                button_style = ""
                if st.session_state.current_page == page_key:
                    button_style = "background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); font-weight: bold;"
                
                if st.button(
                    page_name, 
                    key=f"nav_{page_key}", 
                    use_container_width=True,
                    type="primary" if st.session_state.current_page == page_key else "secondary"
                ):
                    st.session_state.current_page = page_key
                    st.rerun()
        
        st.markdown("---")
        
        # نصيحة اليوم (تحميل عند الحاجة فقط)
        if st.session_state.current_page == "المحادثة":
            try:
                resources_library = load_model('resources')
                daily_tip = resources_library.get_daily_tip()
                st.markdown(f"""
                <div style='background: rgba(76, 175, 80, 0.2); padding: 1rem; border-radius: 10px; color: #4CAF50; margin: 1rem 0; border: 1px solid #4CAF50;'>
                    <h4>{daily_tip['icon']} نصيحة اليوم</h4>
                    <p style='font-size: 0.9rem; margin: 0;'>{daily_tip['tip']}</p>
                </div>
                """, unsafe_allow_html=True)
            except:
                pass
        
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
        
        st.markdown("---")

    # عرض الصفحة المحددة - تحميل محتوى حسب الصفحة فقط
    if st.session_state.current_page == "المحادثة":
        # تحميل المكونات فقط عند الحاجة
        ui_components = load_model('ui')
        
        # العنوان الرئيسي
        ui_components.create_gradient_title(
            "🧠 الطبيب النفسي الذكي", 
            "محادثة سرية وآمنة مع مساعدك الذكي 💚"
        )
        
        # رسالة ترحيبية
        if st.session_state.show_welcome and len(st.session_state.messages) == 0:
            from ui_components import create_welcome_animation
            create_welcome_animation()
            st.session_state.show_welcome = False

        # عرض الرسائل السابقة
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "emotion" in message:
                    st.caption(f"🎭 الحالة: {message['emotion']} | 🤖 {message.get('source', 'AI Model')}")

        # صندوق الإدخال
        if prompt := st.chat_input("اكتب هنا... أنا موجود للاستماع لك 💙"):
            # تحميل النماذج عند الحاجة فقط
            emotion_model = load_model('emotion')
            response_gen = load_model('response')
            mood_tracker = load_model('tracker')
            therapy_exercises = load_model('exercises')
            
            # عرض رسالة المستخدم
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # تحليل المشاعر
            with st.spinner("🔍 بحلل كلامك..."):
                emotion_result = emotion_model.detect_emotion(prompt)
                emotion = emotion_result["emotion"]
                confidence = emotion_result["confidence"]
                description = emotion_result["description_ar"]
            
            # عرض نتيجة التحليل
            ui_components.create_mood_card(emotion, confidence, description)
            
            # توليد الرد
            with st.spinner("💭 بفكر في الرد المناسب..."):
                history_text = ""
                for conv in st.session_state.conversation_history[-3:]:
                    history_text += f"المستخدم: {conv['user']}\nالمساعد: {conv['assistant']}\n"
                
                ai_response = response_gen.generate_ai_response(
                    user_text=prompt,
                    emotion=emotion,
                    history=history_text
                )
            
            # حفظ في نظام تتبع المزاج
            mood_tracker.add_mood_entry(emotion, confidence, prompt, ai_response)
            
            # اقتراح تمرين
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
                "emotion": emotion,
                "source": emotion_result.get('source', 'Unknown')
            })
            
            # عرض الرد
            with st.chat_message("assistant"):
                st.markdown(ai_response)
                st.caption(f"🎭 الحالة: {emotion} | 🤖 النموذج: {emotion_result.get('source', 'Unknown')}")

        # رسالة ترحيبية
        if len(st.session_state.messages) == 0:
            ui_components.create_custom_alert(
                "أهلاً وسهلاً! أنا هنا لأسمعك وأساعدك. احكيلي عن أي شيء في بالك - كل كلامنا سري وآمن 💚",
                "info", "👋"
            )
            
            # عرض مميزات
            features = [
                {"icon": "🎭", "title": "تحليل المشاعر", "description": "فهم حالتك النفسية"},
                {"icon": "🧘", "title": "تمارين مفيدة", "description": "تقنيات الاسترخاء"},
                {"icon": "📊", "title": "تتبع التقدم", "description": "رسوم بيانية للمزاج"},
                {"icon": "📚", "title": "مكتبة الموارد", "description": "نصائح ومقالات"}
            ]
            ui_components.create_feature_grid(features)

    elif st.session_state.current_page == "التحليلات":
        from mood_tracker import display_mood_analytics
        display_mood_analytics()

    elif st.session_state.current_page == "التمارين":
        from therapy_exercises import display_therapy_exercises
        display_therapy_exercises()

    elif st.session_state.current_page == "المكتبة":
        from resources_library import display_resources_library
        display_resources_library()

    elif st.session_state.current_page == "الإعدادات":
        st.header("⚙️ الإعدادات")
        
        st.subheader("🎨 تخصيص الواجهة")
        
        # خيارات الواجهة
        col1, col2 = st.columns(2)
        
        with col1:
            dark_mode = st.checkbox(
                "🌙 الوضع الليلي", 
                value=st.session_state.dark_mode,
                key="dark_mode_checkbox"
            )
            if dark_mode != st.session_state.dark_mode:
                st.session_state.dark_mode = dark_mode
                st.rerun()
            
            if st.session_state.dark_mode:
                st.success("✅ الوضع الليلي مفعل - خلفية غامقة")
            else:
                st.info("☀️ الوضع الفاتح مفعل")
        
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
