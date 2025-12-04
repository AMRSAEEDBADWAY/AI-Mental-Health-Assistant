"""
نظام تتبع الحالة المزاجية والتحليلات
يحفظ البيانات محلياً ويعرض الرسوم البيانية
"""

import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import streamlit as st
from pathlib import Path

class MoodTracker:
    def __init__(self, data_file="data/mood_history.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(exist_ok=True)
        self.mood_data = self.load_data()
    
    def load_data(self):
        """تحميل بيانات الحالة المزاجية"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_data(self):
        """حفظ بيانات الحالة المزاجية"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.mood_data, f, ensure_ascii=False, indent=2)
    
    def add_mood_entry(self, emotion, confidence, user_text, ai_response):
        """إضافة إدخال جديد للحالة المزاجية"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M"),
            "emotion": emotion,
            "confidence": confidence,
            "user_text": user_text[:100] + "..." if len(user_text) > 100 else user_text,
            "ai_response": ai_response[:100] + "..." if len(ai_response) > 100 else ai_response,
            "mood_score": self.emotion_to_score(emotion)
        }
        
        self.mood_data.append(entry)
        self.save_data()
    
    def emotion_to_score(self, emotion):
        """تحويل المشاعر إلى نقاط رقمية للتحليل"""
        scores = {
            'happiness': 5,
            'neutral': 3,
            'anxiety': 2,
            'stress': 2,
            'depression': 1
        }
        return scores.get(emotion, 3)
    
    def get_mood_trends(self, days=30):
        """الحصول على اتجاهات الحالة المزاجية"""
        if not self.mood_data:
            return None
        
        # تحويل إلى DataFrame
        df = pd.DataFrame(self.mood_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # فلترة آخر X أيام
        cutoff_date = datetime.now() - timedelta(days=days)
        df = df[df['timestamp'] >= cutoff_date]
        
        if df.empty:
            return None
        
        return df
    
    def create_mood_chart(self, days=30):
        """إنشاء رسم بياني للحالة المزاجية"""
        df = self.get_mood_trends(days)
        
        if df is None or df.empty:
            return None
        
        # رسم بياني خطي للحالة المزاجية
        fig = px.line(
            df, 
            x='timestamp', 
            y='mood_score',
            title=f'تتبع الحالة المزاجية - آخر {days} يوم',
            labels={
                'timestamp': 'التاريخ',
                'mood_score': 'نقاط المزاج',
                'emotion': 'الحالة'
            },
            color='emotion',
            hover_data=['confidence']
        )
        
        # تخصيص الألوان
        color_map = {
            'happiness': '#2E8B57',  # أخضر
            'neutral': '#4682B4',    # أزرق
            'anxiety': '#FF6347',    # أحمر فاتح
            'stress': '#FF4500',     # برتقالي أحمر
            'depression': '#8B0000'  # أحمر داكن
        }
        
        fig.update_traces(line=dict(width=3))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial", size=12),
            title_font_size=16,
            showlegend=True
        )
        
        return fig
    
    def create_emotion_distribution(self, days=30):
        """إنشاء رسم بياني لتوزيع المشاعر"""
        df = self.get_mood_trends(days)
        
        if df is None or df.empty:
            return None
        
        # حساب توزيع المشاعر
        emotion_counts = df['emotion'].value_counts()
        
        # ترجمة المشاعر للعربية
        emotion_labels = {
            'happiness': 'سعادة',
            'neutral': 'طبيعي',
            'anxiety': 'قلق',
            'stress': 'ضغط',
            'depression': 'حزن'
        }
        
        labels_ar = [emotion_labels.get(emotion, emotion) for emotion in emotion_counts.index]
        
        fig = px.pie(
            values=emotion_counts.values,
            names=labels_ar,
            title=f'توزيع المشاعر - آخر {days} يوم',
            color_discrete_map={
                'سعادة': '#2E8B57',
                'طبيعي': '#4682B4',
                'قلق': '#FF6347',
                'ضغط': '#FF4500',
                'حزن': '#8B0000'
            }
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial", size=12)
        )
        
        return fig
    
    def get_mood_statistics(self, days=30):
        """الحصول على إحصائيات الحالة المزاجية"""
        df = self.get_mood_trends(days)
        
        if df is None or df.empty:
            return None
        
        stats = {
            'total_entries': len(df),
            'average_mood': df['mood_score'].mean(),
            'most_common_emotion': df['emotion'].mode().iloc[0] if not df['emotion'].mode().empty else 'neutral',
            'mood_improvement': self.calculate_mood_trend(df),
            'best_day': df.loc[df['mood_score'].idxmax(), 'date'] if not df.empty else None,
            'worst_day': df.loc[df['mood_score'].idxmin(), 'date'] if not df.empty else None,
            'average_confidence': df['confidence'].mean()
        }
        
        return stats
    
    def calculate_mood_trend(self, df):
        """حساب اتجاه تحسن الحالة المزاجية"""
        if len(df) < 2:
            return 0
        
        # مقارنة النصف الأول بالنصف الثاني
        mid_point = len(df) // 2
        first_half = df.iloc[:mid_point]['mood_score'].mean()
        second_half = df.iloc[mid_point:]['mood_score'].mean()
        
        return second_half - first_half
    
    def get_mood_insights(self, days=30):
        """الحصول على رؤى ذكية حول الحالة المزاجية"""
        stats = self.get_mood_statistics(days)
        
        if not stats:
            return []
        
        insights = []
        
        # تحليل المزاج العام
        if stats['average_mood'] >= 4:
            insights.append("🌟 حالتك المزاجية ممتازة! استمر على هذا المنوال")
        elif stats['average_mood'] >= 3:
            insights.append("😊 حالتك المزاجية جيدة بشكل عام")
        else:
            insights.append("💙 نلاحظ أنك تمر بفترة صعبة، نحن هنا لدعمك")
        
        # تحليل التحسن
        if stats['mood_improvement'] > 0.5:
            insights.append("📈 هناك تحسن ملحوظ في حالتك المزاجية!")
        elif stats['mood_improvement'] < -0.5:
            insights.append("📉 نلاحظ انخفاض في المزاج، ربما تحتاج لمزيد من الدعم")
        
        # تحليل النشاط
        if stats['total_entries'] >= 10:
            insights.append("👏 رائع! أنت تتفاعل بانتظام مع المساعد")
        elif stats['total_entries'] >= 5:
            insights.append("✨ تفاعل جيد! حاول الكتابة أكثر لتتبع أفضل")
        
        # تحليل الثقة
        if stats['average_confidence'] >= 0.8:
            insights.append("🎯 نحن واثقون من تحليل حالتك بدقة عالية")
        
        return insights
    
    def export_data(self, format='csv'):
        """تصدير البيانات"""
        df = pd.DataFrame(self.mood_data)
        
        if format == 'csv':
            return df.to_csv(index=False)
        elif format == 'json':
            return df.to_json(orient='records', force_ascii=False, indent=2)
        
        return None


# دالة مساعدة للاستخدام في Streamlit
def display_mood_analytics():
    """عرض تحليلات الحالة المزاجية في Streamlit"""
    tracker = MoodTracker()
    
    st.header("📊 تحليلات الحالة المزاجية")
    
    # اختيار فترة التحليل
    days = st.selectbox(
        "اختر فترة التحليل:",
        [7, 14, 30, 60, 90],
        index=2,
        format_func=lambda x: f"آخر {x} يوم"
    )
    
    # الإحصائيات
    stats = tracker.get_mood_statistics(days)
    
    if stats:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("إجمالي الإدخالات", stats['total_entries'])
        
        with col2:
            st.metric("متوسط المزاج", f"{stats['average_mood']:.1f}/5")
        
        with col3:
            improvement = stats['mood_improvement']
            st.metric(
                "التحسن", 
                f"{improvement:+.1f}",
                delta=f"{'تحسن' if improvement > 0 else 'انخفاض' if improvement < 0 else 'ثابت'}"
            )
        
        with col4:
            st.metric("دقة التحليل", f"{stats['average_confidence']:.0%}")
        
        # الرسوم البيانية
        col1, col2 = st.columns(2)
        
        with col1:
            mood_chart = tracker.create_mood_chart(days)
            if mood_chart:
                st.plotly_chart(mood_chart, use_container_width=True)
        
        with col2:
            emotion_chart = tracker.create_emotion_distribution(days)
            if emotion_chart:
                st.plotly_chart(emotion_chart, use_container_width=True)
        
        # الرؤى الذكية
        st.subheader("💡 رؤى ذكية")
        insights = tracker.get_mood_insights(days)
        for insight in insights:
            st.info(insight)
        
        # تصدير البيانات
        st.subheader("📤 تصدير البيانات")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("تحميل CSV"):
                csv_data = tracker.export_data('csv')
                st.download_button(
                    label="تحميل ملف CSV",
                    data=csv_data,
                    file_name=f"mood_data_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
        
        with col2:
            if st.button("تحميل JSON"):
                json_data = tracker.export_data('json')
                st.download_button(
                    label="تحميل ملف JSON",
                    data=json_data,
                    file_name=f"mood_data_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )
    
    else:
        st.info("لا توجد بيانات كافية للتحليل. ابدأ بالتحدث مع المساعد لتجميع البيانات!")


if __name__ == "__main__":
    # اختبار سريع
    tracker = MoodTracker()
    
    # إضافة بيانات تجريبية
    import random
    emotions = ['happiness', 'neutral', 'anxiety', 'stress', 'depression']
    
    for i in range(20):
        emotion = random.choice(emotions)
        confidence = random.uniform(0.6, 0.95)
        tracker.add_mood_entry(
            emotion=emotion,
            confidence=confidence,
            user_text=f"نص تجريبي {i+1}",
            ai_response=f"رد تجريبي {i+1}"
        )
    
    print("تم إضافة بيانات تجريبية!")
    stats = tracker.get_mood_statistics()
    print("الإحصائيات:", stats)


