"""
نظام إدارة الذاكرة المتقدم
مسؤول عن تخزين المحادثة، تتبع السياق، وتلخيص الجلسة
"""

import streamlit as st
from datetime import datetime

class MemoryManager:
    def __init__(self, max_history=15):
        self.max_history = max_history
        self._initialize_session_state()

    def _initialize_session_state(self):
        """تهيئة متغيرات الجلسة"""
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []
        if 'session_summary' not in st.session_state:
            st.session_state.session_summary = ""
        if 'mood_history' not in st.session_state:
            st.session_state.mood_history = []
        if 'user_concerns' not in st.session_state:
            st.session_state.user_concerns = []

    def add_message(self, role, content, emotion=None):
        """إضافة رسالة جديدة للذاكرة"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "emotion": emotion
        }
        st.session_state.conversation_history.append(message)
        
        # الحفاظ على حجم الذاكرة
        if len(st.session_state.conversation_history) > self.max_history:
            # الاحتفاظ بأول رسالة (السياق الأولي) وآخر N رسائل
            first_msg = st.session_state.conversation_history[0]
            recent_msgs = st.session_state.conversation_history[-(self.max_history-1):]
            st.session_state.conversation_history = [first_msg] + recent_msgs

    def get_history_text(self):
        """تحويل التاريخ لنص يمكن إرساله للنموذج"""
        history_text = ""
        for msg in st.session_state.conversation_history:
            role_ar = "المستخدم" if msg["role"] == "user" else "المعالج"
            emotion_tag = f"[{msg['emotion']}]" if msg.get("emotion") else ""
            history_text += f"{role_ar} {emotion_tag}: {msg['content']}\n"
        return history_text

    def track_mood(self, emotion, confidence):
        """تتبع الحالة المزاجية خلال الجلسة"""
        st.session_state.mood_history.append({
            "emotion": emotion,
            "confidence": confidence,
            "timestamp": datetime.now().strftime("%H:%M")
        })

    def get_session_mood_trend(self):
        """الحصول على اتجاه المزاج في الجلسة الحالية"""
        return st.session_state.mood_history

    def extract_concerns(self, text):
        """(مبسط) استخراج الاهتمامات الرئيسية من النص"""
        # يمكن تطويره لاستخدام AI لاحقاً
        # حالياً نقوم بتخزين آخر اهتمام للمستخدم
        pass

    def clear_memory(self):
        """مسح الذاكرة"""
        st.session_state.conversation_history = []
        st.session_state.mood_history = []
        st.session_state.session_summary = ""
