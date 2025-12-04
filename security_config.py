"""
نظام الحماية والأمان للتطبيق
حماية بكلمة مرور والوصول المحدود
"""

import streamlit as st
import hashlib
import os

class SecurityManager:
    """مدير الأمان للتطبيق"""
    
    def __init__(self):
        # كلمة المرور الافتراضية (يجب تغييرها في Secrets)
        self.password_hash = self.get_password_hash()
    
    def get_password_hash(self):
        """الحصول على hash كلمة المرور من Secrets أو .env"""
        # محاولة قراءة من Streamlit Secrets أولاً
        try:
            password = st.secrets.get("APP_PASSWORD", None)
        except:
            password = None
        
        # إذا لم يكن في Secrets، اقرأ من .env
        if not password:
            from dotenv import load_dotenv
            load_dotenv()
            password = os.getenv("APP_PASSWORD", "admin123")  # كلمة مرور افتراضية
        
        # تشفير كلمة المرور
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        """التحقق من كلمة المرور"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash == self.password_hash
    
    def check_authentication(self):
        """التحقق من المصادقة"""
        # التحقق من حالة المصادقة
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        
        if 'login_attempts' not in st.session_state:
            st.session_state.login_attempts = 0
        
        # إذا لم يكن مصرحاً، عرض صفحة تسجيل الدخول
        if not st.session_state.authenticated:
            self.show_login_page()
            return False
        
        return True
    
    def show_login_page(self):
        """عرض صفحة تسجيل الدخول"""
        st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 2rem;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-radius: 15px;
            border: 1px solid #2d3748;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        .login-title {
            text-align: center;
            color: #e0e0e0;
            margin-bottom: 2rem;
        }
        .stTextInput > div > div > input {
            background: rgba(22, 33, 62, 0.8);
            color: #e0e0e0;
            border: 1px solid #2d3748;
        }
        </style>
        
        <div class="login-container">
            <h1 class="login-title">🔒 تطبيق محمي</h1>
            <p style="text-align: center; color: #a0a0a0; margin-bottom: 2rem;">
                يرجى إدخال كلمة المرور للوصول
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # صفحة تسجيل الدخول
        with st.form("login_form"):
            password = st.text_input(
                "كلمة المرور:",
                type="password",
                help="أدخل كلمة المرور للوصول للتطبيق"
            )
            
            submit_button = st.form_submit_button("دخول 🔐", use_container_width=True)
            
            if submit_button:
                if self.verify_password(password):
                    st.session_state.authenticated = True
                    st.session_state.login_attempts = 0
                    st.success("تم تسجيل الدخول بنجاح! ✅")
                    st.rerun()
                else:
                    st.session_state.login_attempts += 1
                    if st.session_state.login_attempts >= 3:
                        st.error("⚠️ لقد تجاوزت عدد المحاولات المسموح به. يرجى المحاولة لاحقاً.")
                        st.stop()
                    else:
                        st.error(f"❌ كلمة المرور غير صحيحة. المحاولات المتبقية: {3 - st.session_state.login_attempts}")
        
        # معلومات إضافية
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; margin-top: 2rem;">
            <small>© 2024 AI Mental Health Assistant - تطبيق محمي</small>
        </div>
        """, unsafe_allow_html=True)
    
    def logout(self):
        """تسجيل الخروج"""
        st.session_state.authenticated = False
        st.session_state.login_attempts = 0
        st.rerun()


def require_password():
    """دالة مساعدة للتحقق من كلمة المرور"""
    security = SecurityManager()
    if not security.check_authentication():
        st.stop()
    return security
