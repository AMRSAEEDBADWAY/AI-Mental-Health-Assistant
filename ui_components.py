"""
مكونات واجهة المستخدم المحسنة
تشمل تصميمات جميلة وتفاعلية للتطبيق
"""

import streamlit as st
import base64
from pathlib import Path

class UIComponents:
    def __init__(self):
        self.load_custom_css()
    
    def load_custom_css(self):
        """تحميل CSS مخصص للتطبيق"""
        css = """
        <style>
        /* الخطوط والألوان الأساسية */
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Cairo', sans-serif;
            direction: rtl;
        }
        
        /* الألوان الرئيسية */
        :root {
            --primary-color: #4CAF50;
            --secondary-color: #2196F3;
            --accent-color: #FF9800;
            --success-color: #8BC34A;
            --warning-color: #FFC107;
            --error-color: #F44336;
            --background-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --card-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* الخلفية الرئيسية */
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        /* البطاقات */
        .custom-card {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: var(--card-shadow);
            margin: 1rem 0;
            border-left: 4px solid var(--primary-color);
        }
        
        .mood-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin: 1rem 0;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        
        .exercise-card {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .exercise-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        
        /* الأزرار */
        .stButton > button {
            background: var(--background-gradient);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: var(--card-shadow);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        
        /* شريط التقدم */
        .stProgress > div > div > div > div {
            background: var(--background-gradient);
            border-radius: 10px;
        }
        
        /* الرسائل */
        .chat-message {
            padding: 1rem;
            border-radius: 15px;
            margin: 0.5rem 0;
            max-width: 80%;
        }
        
        .user-message {
            background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
            color: white;
            margin-left: auto;
            text-align: right;
        }
        
        .assistant-message {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            margin-right: auto;
            text-align: right;
        }
        
        /* الإحصائيات */
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: var(--card-shadow);
            border-top: 4px solid var(--primary-color);
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary-color);
        }
        
        .metric-label {
            color: #666;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }
        
        /* الشريط الجانبي */
        .css-1d391kg {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        .css-1d391kg .css-1v0mbdj {
            color: white;
        }
        
        /* التنبيهات */
        .custom-alert {
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            border-left: 4px solid;
        }
        
        .alert-success {
            background: #d4edda;
            border-color: #28a745;
            color: #155724;
        }
        
        .alert-info {
            background: #d1ecf1;
            border-color: #17a2b8;
            color: #0c5460;
        }
        
        .alert-warning {
            background: #fff3cd;
            border-color: #ffc107;
            color: #856404;
        }
        
        .alert-error {
            background: #f8d7da;
            border-color: #dc3545;
            color: #721c24;
        }
        
        /* الرسوم المتحركة */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.5s ease-out;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        /* الوضع الليلي */
        .dark-mode {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
        }
        
        .dark-mode .custom-card {
            background: #34495e;
            color: white;
        }
        
        /* تحسينات الجوال */
        @media (max-width: 768px) {
            .custom-card {
                padding: 1rem;
                margin: 0.5rem 0;
            }
            
            .mood-card {
                padding: 1.5rem;
            }
            
            .chat-message {
                max-width: 95%;
            }
        }
        
        /* تأثيرات خاصة */
        .breathing-circle {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: var(--background-gradient);
            margin: 2rem auto;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            font-weight: 600;
        }
        
        .breathing-inhale {
            animation: breatheIn 4s ease-in-out infinite;
        }
        
        .breathing-exhale {
            animation: breatheOut 6s ease-in-out infinite;
        }
        
        @keyframes breatheIn {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
        
        @keyframes breatheOut {
            0%, 100% { transform: scale(1.2); }
            50% { transform: scale(1); }
        }
        
        /* تحسينات النصوص */
        .title-gradient {
            background: var(--background-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
        }
        
        .subtitle {
            color: #666;
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }
        
        /* تحسينات الأيقونات */
        .icon-large {
            font-size: 3rem;
            margin: 1rem 0;
        }
        
        .icon-medium {
            font-size: 2rem;
            margin: 0.5rem;
        }
        
        .icon-small {
            font-size: 1.2rem;
            margin: 0.2rem;
        }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

    def get_dark_mode_css(self):
        """إرجاع CSS للوضع الليلي"""
        return """
        <style>
        /* تحسينات الأداء */
        * {
            transition: none !important;
            animation-duration: 0.2s !important;
        }
        
        /* الوضع الليلي الكامل */
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%) !important;
            color: #e0e0e0 !important;
        }
        
        /* الخلفية الرئيسية */
        .main {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%) !important;
        }
        
        /* تحسين سرعة التحميل */
        img, iframe {
            loading: lazy;
        }
        
        /* الشريط الجانبي */
        .css-1d391kg {
            background: linear-gradient(180deg, #16213e 0%, #0f3460 100%);
            border-right: 1px solid #2d3748;
        }
        
        /* النصوص */
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: #e0e0e0 !important;
        }
        
        /* البطاقات */
        .element-container {
            background: rgba(26, 26, 46, 0.8);
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
            border: 1px solid #2d3748;
        }
        
        /* محادثات Streamlit */
        .stChatMessage {
            background: rgba(22, 33, 62, 0.9) !important;
            border: 1px solid #2d3748;
        }
        
        .stChatMessage[data-testid="user"] {
            background: rgba(26, 95, 180, 0.3) !important;
        }
        
        .stChatMessage[data-testid="assistant"] {
            background: rgba(15, 52, 96, 0.5) !important;
        }
        
        /* الأزرار */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        
        /* حقول الإدخال */
        .stTextInput > div > div > input {
            background: rgba(22, 33, 62, 0.8);
            color: #e0e0e0;
            border: 1px solid #2d3748;
        }
        
        .stTextInput > div > div > input:focus {
            border: 1px solid #667eea;
            box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
        }
        
        /* محادثة الدردشة */
        .stChatInput {
            background: rgba(22, 33, 62, 0.9);
            border-top: 1px solid #2d3748;
        }
        
        /* التبويبات */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(22, 33, 62, 0.5);
            border-bottom: 1px solid #2d3748;
        }
        
        .stTabs [data-baseweb="tab"] {
            color: #a0a0a0;
            border-bottom: 2px solid transparent;
        }
        
        .stTabs [aria-selected="true"] {
            color: #667eea !important;
            border-bottom: 2px solid #667eea;
        }
        
        /* التنبيهات */
        .stAlert {
            background: rgba(22, 33, 62, 0.9);
            border: 1px solid #2d3748;
            border-left: 4px solid #667eea;
        }
        
        .stSuccess {
            background: rgba(15, 52, 96, 0.9);
            border-left: 4px solid #4CAF50;
        }
        
        .stInfo {
            background: rgba(15, 52, 96, 0.9);
            border-left: 4px solid #2196F3;
        }
        
        .stWarning {
            background: rgba(26, 46, 62, 0.9);
            border-left: 4px solid #FF9800;
        }
        
        .stError {
            background: rgba(62, 22, 22, 0.9);
            border-left: 4px solid #F44336;
        }
        
        /* الرسوم البيانية */
        .js-plotly-plot {
            background: rgba(22, 33, 62, 0.5) !important;
        }
        
        /* جداول البيانات */
        .stDataFrame {
            background: rgba(22, 33, 62, 0.8);
            color: #e0e0e0;
        }
        
        /* شريط التقدم */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }
        
        /* المحددات */
        .stSelectbox > div > div {
            background: rgba(22, 33, 62, 0.8);
            color: #e0e0e0;
            border: 1px solid #2d3748;
        }
        
        /* مربعات الاختيار */
        .stCheckbox {
            color: #e0e0e0;
        }
        
        /* شريط التمرير */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1a2e;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #667eea;
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #764ba2;
        }
        
        /* تحسينات إضافية */
        .stMarkdown {
            color: #e0e0e0;
        }
        
        /* البطاقات المخصصة */
        .custom-card {
            background: rgba(22, 33, 62, 0.9) !important;
            border: 1px solid #2d3748 !important;
            color: #e0e0e0 !important;
        }
        
        /* الروابط */
        a {
            color: #667eea !important;
        }
        
        a:hover {
            color: #764ba2 !important;
        }
        </style>
        """
    
    def create_mood_card(self, emotion, confidence, description):
        """إنشاء بطاقة الحالة المزاجية"""
        emotion_colors = {
            'happiness': '#4CAF50',
            'neutral': '#2196F3',
            'anxiety': '#FF9800',
            'stress': '#FF5722',
            'depression': '#9C27B0'
        }
        
        emotion_icons = {
            'happiness': '😊',
            'neutral': '😐',
            'anxiety': '😰',
            'stress': '😫',
            'depression': '😢'
        }
        
        color = emotion_colors.get(emotion, '#2196F3')
        icon = emotion_icons.get(emotion, '🙂')
        
        st.markdown(f"""
        <div class="mood-card fade-in" style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%);">
            <div class="icon-large">{icon}</div>
            <h2>الحالة المكتشفة</h2>
            <h3>{description}</h3>
            <p>دقة التحليل: {confidence:.0%}</p>
        </div>
        """, unsafe_allow_html=True)
    
    def create_metric_card(self, title, value, delta=None, icon="📊"):
        """إنشاء بطاقة إحصائية"""
        delta_html = ""
        if delta:
            delta_color = "#4CAF50" if delta > 0 else "#F44336" if delta < 0 else "#666"
            delta_arrow = "↗️" if delta > 0 else "↘️" if delta < 0 else "➡️"
            delta_html = f'<div style="color: {delta_color}; font-size: 0.9rem;">{delta_arrow} {delta:+.1f}</div>'
        
        st.markdown(f"""
        <div class="metric-card fade-in">
            <div class="icon-medium">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{title}</div>
            {delta_html}
        </div>
        """, unsafe_allow_html=True)
    
    def create_exercise_card(self, title, description, icon, duration):
        """إنشاء بطاقة تمرين"""
        st.markdown(f"""
        <div class="exercise-card fade-in">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0;">{icon} {title}</h3>
                    <p style="margin: 0.5rem 0; opacity: 0.9;">{description}</p>
                    <small style="opacity: 0.8;">⏱️ {duration} دقائق</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_progress_ring(self, progress, title, color="#4CAF50"):
        """إنشاء حلقة تقدم دائرية"""
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <div style="position: relative; width: 120px; height: 120px; margin: 0 auto;">
                <svg width="120" height="120" style="transform: rotate(-90deg);">
                    <circle cx="60" cy="60" r="50" fill="none" stroke="#e0e0e0" stroke-width="8"/>
                    <circle cx="60" cy="60" r="50" fill="none" stroke="{color}" stroke-width="8"
                            stroke-dasharray="{2 * 3.14159 * 50}" 
                            stroke-dashoffset="{2 * 3.14159 * 50 * (1 - progress)}"
                            style="transition: stroke-dashoffset 0.5s ease;"/>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                           font-size: 1.5rem; font-weight: 600; color: {color};">
                    {progress:.0%}
                </div>
            </div>
            <h4 style="margin-top: 1rem; color: #666;">{title}</h4>
        </div>
        """, unsafe_allow_html=True)
    
    def create_breathing_circle(self, phase="inhale"):
        """إنشاء دائرة التنفس المتحركة"""
        animation_class = "breathing-inhale" if phase == "inhale" else "breathing-exhale"
        phase_text = "استنشق" if phase == "inhale" else "أخرج الهواء"
        
        st.markdown(f"""
        <div class="breathing-circle {animation_class}">
            {phase_text}
        </div>
        """, unsafe_allow_html=True)
    
    def create_custom_alert(self, message, alert_type="info", icon=None):
        """إنشاء تنبيه مخصص"""
        icons = {
            "success": "✅",
            "info": "ℹ️",
            "warning": "⚠️",
            "error": "❌"
        }
        
        alert_icon = icon or icons.get(alert_type, "ℹ️")
        
        st.markdown(f"""
        <div class="custom-alert alert-{alert_type} fade-in">
            <strong>{alert_icon} {message}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    def create_gradient_title(self, title, subtitle=None):
        """إنشاء عنوان بتدرج لوني"""
        subtitle_html = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
        
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <h1 class="title-gradient">{title}</h1>
            {subtitle_html}
        </div>
        """, unsafe_allow_html=True)
    
    def create_feature_grid(self, features):
        """إنشاء شبكة المميزات"""
        cols = st.columns(len(features))
        
        for i, feature in enumerate(features):
            with cols[i]:
                st.markdown(f"""
                <div class="custom-card fade-in" style="text-align: center;">
                    <div class="icon-large">{feature['icon']}</div>
                    <h4>{feature['title']}</h4>
                    <p style="color: #666; font-size: 0.9rem;">{feature['description']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    def create_timeline_item(self, time, title, description, icon="🕐"):
        """إنشاء عنصر في الخط الزمني"""
        st.markdown(f"""
        <div class="custom-card fade-in" style="border-left: 4px solid #4CAF50; margin-left: 2rem;">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 1.2rem; margin-left: 0.5rem;">{icon}</span>
                <small style="color: #666; font-weight: 600;">{time}</small>
            </div>
            <h4 style="margin: 0.5rem 0;">{title}</h4>
            <p style="color: #666; margin: 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)
    
    def add_floating_particles(self):
        """إضافة جسيمات متحركة في الخلفية"""
        st.markdown("""
        <div id="particles-js" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>
        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
        <script>
        particlesJS('particles-js', {
            particles: {
                number: { value: 50 },
                color: { value: '#667eea' },
                shape: { type: 'circle' },
                opacity: { value: 0.3 },
                size: { value: 3 },
                move: { enable: true, speed: 1 }
            }
        });
        </script>
        """, unsafe_allow_html=True)
    
    def create_mood_emoji_selector(self):
        """إنشاء محدد الحالة المزاجية بالإيموجي"""
        st.markdown("### كيف تشعر الآن؟")
        
        moods = [
            {"emoji": "😊", "label": "سعيد", "value": "happiness"},
            {"emoji": "😐", "label": "طبيعي", "value": "neutral"},
            {"emoji": "😰", "label": "قلق", "value": "anxiety"},
            {"emoji": "😫", "label": "متوتر", "value": "stress"},
            {"emoji": "😢", "label": "حزين", "value": "depression"}
        ]
        
        cols = st.columns(len(moods))
        selected_mood = None
        
        for i, mood in enumerate(moods):
            with cols[i]:
                if st.button(f"{mood['emoji']}\n{mood['label']}", key=f"mood_{mood['value']}"):
                    selected_mood = mood['value']
        
        return selected_mood


def apply_dark_mode():
    """تطبيق الوضع الليلي"""
    st.markdown("""
    <script>
    document.body.classList.add('dark-mode');
    </script>
    """, unsafe_allow_html=True)


def create_welcome_animation():
    """إنشاء رسوم متحركة ترحيبية"""
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <div class="pulse" style="font-size: 4rem; margin-bottom: 1rem;">🧠</div>
        <h1 class="title-gradient fade-in">مرحباً بك في مساعدك النفسي الذكي</h1>
        <p class="subtitle fade-in">نحن هنا لدعمك ومساعدتك على فهم مشاعرك</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    # اختبار المكونات
    ui = UIComponents()
    
    # اختبار بطاقة المزاج
    ui.create_mood_card("happiness", 0.85, "حالة سعادة وراحة")
    
    # اختبار بطاقة الإحصائيات
    ui.create_metric_card("متوسط المزاج", "4.2/5", 0.3, "📊")
    
    print("تم تحميل مكونات الواجهة بنجاح!")


