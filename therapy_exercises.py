"""
تمارين وتقنيات العلاج النفسي التفاعلية
تشمل تمارين التنفس، الاسترخاء، واليقظة الذهنية
"""

import streamlit as st
import time
import random
from datetime import datetime
import json
from pathlib import Path

class TherapyExercises:
    def __init__(self):
        self.exercises_data = self.load_exercises_data()
        self.user_progress = self.load_user_progress()
    
    def load_exercises_data(self):
        """تحميل بيانات التمارين"""
        return {
            "breathing": {
                "name": "تمارين التنفس",
                "icon": "🫁",
                "exercises": [
                    {
                        "name": "تنفس 4-7-8",
                        "description": "تقنية مهدئة للقلق والتوتر",
                        "steps": [
                            "اجلس في وضع مريح",
                            "ضع طرف لسانك خلف أسنانك العلوية",
                            "أخرج الهواء تماماً من فمك",
                            "أغلق فمك واستنشق من الأنف لمدة 4 ثوانِ",
                            "احبس النفس لمدة 7 ثوانِ",
                            "أخرج الهواء من الفم لمدة 8 ثوانِ",
                            "كرر 3-4 مرات"
                        ],
                        "duration": 2,
                        "benefits": ["تقليل القلق", "تحسين النوم", "الاسترخاء السريع"]
                    },
                    {
                        "name": "التنفس العميق",
                        "description": "تنفس بطيء وعميق للاسترخاء",
                        "steps": [
                            "اجلس أو استلق بشكل مريح",
                            "ضع يد على صدرك ويد على بطنك",
                            "تنفس ببطء من الأنف",
                            "اجعل بطنك يرتفع أكثر من صدرك",
                            "أخرج الهواء ببطء من الفم",
                            "كرر لمدة 5-10 دقائق"
                        ],
                        "duration": 5,
                        "benefits": ["تقليل الضغط", "تحسين التركيز", "الهدوء النفسي"]
                    }
                ]
            },
            "mindfulness": {
                "name": "اليقظة الذهنية",
                "icon": "🧘",
                "exercises": [
                    {
                        "name": "تأمل الـ 5 حواس",
                        "description": "تركيز على اللحظة الحالية",
                        "steps": [
                            "اجلس في مكان هادئ",
                            "حدد 5 أشياء تراها",
                            "حدد 4 أشياء تلمسها",
                            "حدد 3 أشياء تسمعها",
                            "حدد شيئين تشمهما",
                            "حدد شيء واحد تتذوقه",
                            "خذ نفساً عميقاً واسترخ"
                        ],
                        "duration": 3,
                        "benefits": ["تقليل القلق", "زيادة التركيز", "الحضور الذهني"]
                    },
                    {
                        "name": "مسح الجسم",
                        "description": "استرخاء تدريجي لكامل الجسم",
                        "steps": [
                            "استلق بشكل مريح",
                            "أغلق عينيك وتنفس بعمق",
                            "ركز على أصابع قدميك - استرخها",
                            "انتقل تدريجياً لأعلى الجسم",
                            "استرخ كل عضلة تمر عليها",
                            "وصل للرأس والوجه",
                            "استمتع بالاسترخاء الكامل"
                        ],
                        "duration": 10,
                        "benefits": ["استرخاء عميق", "تقليل التوتر العضلي", "تحسين النوم"]
                    }
                ]
            },
            "cognitive": {
                "name": "التمارين المعرفية",
                "icon": "🧠",
                "exercises": [
                    {
                        "name": "تحدي الأفكار السلبية",
                        "description": "إعادة تقييم الأفكار المؤذية",
                        "steps": [
                            "اكتب الفكرة السلبية",
                            "اسأل: هل هذا صحيح 100%؟",
                            "ما الدليل على صحة هذه الفكرة؟",
                            "ما الدليل ضد هذه الفكرة؟",
                            "ما رأي صديق حكيم؟",
                            "اكتب فكرة أكثر توازناً",
                            "كيف تشعر الآن؟"
                        ],
                        "duration": 5,
                        "benefits": ["تقليل الأفكار السلبية", "تحسين المزاج", "زيادة الوعي الذاتي"]
                    }
                ]
            },
            "gratitude": {
                "name": "تمارين الامتنان",
                "icon": "🙏",
                "exercises": [
                    {
                        "name": "يومية الامتنان",
                        "description": "كتابة 3 أشياء تشعر بالامتنان لها",
                        "steps": [
                            "اجلس في مكان هادئ",
                            "فكر في يومك",
                            "اكتب 3 أشياء تشعر بالامتنان لها",
                            "اكتب لماذا تشعر بالامتنان لكل شيء",
                            "تأمل في هذه المشاعر الإيجابية",
                            "احتفظ بهذه القائمة"
                        ],
                        "duration": 5,
                        "benefits": ["تحسين المزاج", "زيادة السعادة", "تقليل الاكتئاب"]
                    }
                ]
            }
        }
    
    def load_user_progress(self):
        """تحميل تقدم المستخدم"""
        progress_file = Path("data/exercise_progress.json")
        if progress_file.exists():
            try:
                with open(progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_user_progress(self):
        """حفظ تقدم المستخدم"""
        progress_file = Path("data/exercise_progress.json")
        progress_file.parent.mkdir(exist_ok=True)
        
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.user_progress, f, ensure_ascii=False, indent=2)
    
    def record_exercise_completion(self, category, exercise_name, rating=None):
        """تسجيل إكمال تمرين"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        if today not in self.user_progress:
            self.user_progress[today] = {}
        
        if category not in self.user_progress[today]:
            self.user_progress[today][category] = []
        
        completion_record = {
            "exercise": exercise_name,
            "time": datetime.now().strftime("%H:%M"),
            "rating": rating
        }
        
        self.user_progress[today][category].append(completion_record)
        self.save_user_progress()
    
    def get_daily_challenge(self):
        """الحصول على تحدي يومي"""
        challenges = [
            {
                "title": "تحدي الامتنان",
                "description": "اكتب 5 أشياء تشعر بالامتنان لها اليوم",
                "icon": "🌟",
                "category": "gratitude"
            },
            {
                "title": "تحدي التنفس",
                "description": "مارس تمرين التنفس العميق لمدة 5 دقائق",
                "icon": "🫁",
                "category": "breathing"
            },
            {
                "title": "تحدي اليقظة",
                "description": "مارس تأمل الـ 5 حواس",
                "icon": "🧘",
                "category": "mindfulness"
            },
            {
                "title": "تحدي الأفكار",
                "description": "تحدى فكرة سلبية واحدة اليوم",
                "icon": "💭",
                "category": "cognitive"
            }
        ]
        
        # اختيار تحدي عشوائي أو بناءً على التاريخ
        today_seed = int(datetime.now().strftime("%Y%m%d"))
        random.seed(today_seed)
        return random.choice(challenges)
    
    def get_recommended_exercise(self, emotion):
        """اقتراح تمرين بناءً على الحالة النفسية"""
        recommendations = {
            'anxiety': {
                'category': 'breathing',
                'exercise': 'تنفس 4-7-8',
                'reason': 'تمرين التنفس هذا فعال جداً في تهدئة القلق'
            },
            'stress': {
                'category': 'mindfulness',
                'exercise': 'مسح الجسم',
                'reason': 'يساعد على تخفيف التوتر الجسدي والنفسي'
            },
            'depression': {
                'category': 'gratitude',
                'exercise': 'يومية الامتنان',
                'reason': 'التركيز على الإيجابيات يحسن المزاج'
            },
            'neutral': {
                'category': 'mindfulness',
                'exercise': 'تأمل الـ 5 حواس',
                'reason': 'يزيد من الوعي والحضور الذهني'
            }
        }
        
        return recommendations.get(emotion, recommendations['neutral'])
    
    def create_guided_breathing_timer(self, exercise_type="deep"):
        """إنشاء مؤقت تنفس مرشد"""
        if exercise_type == "4-7-8":
            pattern = [(4, "استنشق"), (7, "احبس"), (8, "أخرج الهواء")]
            cycles = 4
        else:  # deep breathing
            pattern = [(4, "استنشق"), (6, "أخرج الهواء")]
            cycles = 10
        
        return pattern, cycles


def display_breathing_exercise():
    """عرض تمرين التنفس التفاعلي"""
    st.subheader("🫁 تمرين التنفس التفاعلي")
    
    exercise_type = st.selectbox(
        "اختر نوع التمرين:",
        ["التنفس العميق", "تنفس 4-7-8"],
        key="breathing_type"
    )
    
    if st.button("ابدأ التمرين", key="start_breathing"):
        exercises = TherapyExercises()
        
        if exercise_type == "تنفس 4-7-8":
            pattern, cycles = exercises.create_guided_breathing_timer("4-7-8")
        else:
            pattern, cycles = exercises.create_guided_breathing_timer("deep")
        
        # إنشاء placeholder للتحديث المباشر
        placeholder = st.empty()
        progress_bar = st.progress(0)
        
        # حساب المدة الكلية بالثواني
        cycle_duration = sum(step[0] for step in pattern)
        total_duration = cycles * cycle_duration
        elapsed_seconds = 0
        
        for cycle in range(cycles):
            for step_duration, instruction in pattern:
                for second in range(step_duration):
                    with placeholder.container():
                        st.markdown(f"""
                        <div style='text-align: center; padding: 2rem;'>
                            <h2 style='color: #4CAF50;'>{instruction}</h2>
                            <h1 style='font-size: 4rem; color: #2196F3;'>{step_duration - second}</h1>
                            <p>الدورة {cycle + 1} من {cycles}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # تحديث التقدم
                    elapsed_seconds += 1
                    progress = min(elapsed_seconds / total_duration, 1.0)
                    progress_bar.progress(progress)
                    
                    time.sleep(1)
        
        placeholder.success("🎉 أحسنت! أكملت التمرين بنجاح")
        
        # تقييم التمرين
        rating = st.slider("كيف تشعر الآن؟", 1, 5, 3, key="breathing_rating")
        if st.button("حفظ التقييم", key="save_breathing"):
            exercises.record_exercise_completion("breathing", exercise_type, rating)
            st.success("تم حفظ تقدمك!")


def display_mindfulness_exercise():
    """عرض تمرين اليقظة الذهنية"""
    st.subheader("🧘 تمرين اليقظة الذهنية")
    
    exercises = TherapyExercises()
    mindfulness_exercises = exercises.exercises_data["mindfulness"]["exercises"]
    
    selected_exercise = st.selectbox(
        "اختر التمرين:",
        [ex["name"] for ex in mindfulness_exercises],
        key="mindfulness_select"
    )
    
    # عرض تفاصيل التمرين
    exercise_data = next(ex for ex in mindfulness_exercises if ex["name"] == selected_exercise)
    
    st.write(f"**الوصف:** {exercise_data['description']}")
    st.write(f"**المدة:** {exercise_data['duration']} دقائق")
    st.write(f"**الفوائد:** {', '.join(exercise_data['benefits'])}")
    
    with st.expander("خطوات التمرين"):
        for i, step in enumerate(exercise_data["steps"], 1):
            st.write(f"{i}. {step}")
    
    if st.button("بدأت التمرين", key="start_mindfulness"):
        st.success("ممتاز! خذ وقتك واتبع الخطوات بهدوء")
        
        # مؤقت بسيط
        duration_minutes = exercise_data["duration"]
        placeholder = st.empty()
        progress_bar = st.progress(0)
        
        for minute in range(duration_minutes):
            for second in range(60):
                remaining_seconds = (duration_minutes * 60) - (minute * 60 + second)
                minutes_left = remaining_seconds // 60
                seconds_left = remaining_seconds % 60
                
                with placeholder.container():
                    st.markdown(f"""
                    <div style='text-align: center; padding: 1rem;'>
                        <h3>⏰ الوقت المتبقي: {minutes_left:02d}:{seconds_left:02d}</h3>
                        <p style='color: #666;'>تنفس بهدوء واتبع الخطوات</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                progress = (minute * 60 + second + 1) / (duration_minutes * 60)
                progress_bar.progress(progress)
                
                time.sleep(1)
        
        placeholder.success("🎉 رائع! أكملت تمرين اليقظة الذهنية")
        
        # تقييم
        rating = st.slider("كيف كانت تجربتك؟", 1, 5, 4, key="mindfulness_rating")
        if st.button("حفظ التقييم", key="save_mindfulness"):
            exercises.record_exercise_completion("mindfulness", selected_exercise, rating)
            st.success("تم حفظ تقدمك!")


def display_daily_challenge():
    """عرض التحدي اليومي"""
    exercises = TherapyExercises()
    challenge = exercises.get_daily_challenge()
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 15px; color: white; text-align: center;'>
        <h2>{challenge['icon']} تحدي اليوم</h2>
        <h3>{challenge['title']}</h3>
        <p style='font-size: 1.1rem;'>{challenge['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("أكملت التحدي! 🎉", key="complete_challenge"):
        exercises.record_exercise_completion(challenge['category'], challenge['title'], 5)
        st.balloons()
        st.success("مبروك! أكملت تحدي اليوم بنجاح!")


def display_therapy_exercises():
    """عرض جميع التمارين العلاجية"""
    st.header("🧘 التمارين والتقنيات النفسية")
    
    # التحدي اليومي
    with st.container():
        display_daily_challenge()
    
    st.markdown("---")
    
    # اختيار نوع التمرين
    tab1, tab2, tab3, tab4 = st.tabs(["🫁 التنفس", "🧘 اليقظة الذهنية", "🧠 المعرفي", "🙏 الامتنان"])
    
    with tab1:
        display_breathing_exercise()
    
    with tab2:
        display_mindfulness_exercise()
    
    with tab3:
        st.subheader("🧠 التمارين المعرفية")
        st.info("قريباً: تمارين تفاعلية لتحدي الأفكار السلبية")
    
    with tab4:
        st.subheader("🙏 تمارين الامتنان")
        
        st.write("اكتب 3 أشياء تشعر بالامتنان لها اليوم:")
        
        gratitude1 = st.text_input("الشيء الأول:", key="gratitude1")
        gratitude2 = st.text_input("الشيء الثاني:", key="gratitude2")
        gratitude3 = st.text_input("الشيء الثالث:", key="gratitude3")
        
        if st.button("حفظ قائمة الامتنان", key="save_gratitude"):
            if gratitude1 and gratitude2 and gratitude3:
                exercises = TherapyExercises()
                gratitude_list = f"{gratitude1}, {gratitude2}, {gratitude3}"
                exercises.record_exercise_completion("gratitude", "يومية الامتنان", 5)
                st.success("تم حفظ قائمة الامتنان! 🙏")
                st.balloons()
            else:
                st.warning("يرجى ملء جميع الحقول")


if __name__ == "__main__":
    # اختبار التمارين
    exercises = TherapyExercises()
    print("تم تحميل التمارين بنجاح!")
    
    # اختبار التحدي اليومي
    challenge = exercises.get_daily_challenge()
    print(f"تحدي اليوم: {challenge['title']}")
    
    # اختبار التوصيات
    recommendation = exercises.get_recommended_exercise('anxiety')
    print(f"التوصية للقلق: {recommendation['exercise']}")


