"""
مكتبة الموارد والنصائح النفسية
تحتوي على مقالات، نصائح، وموارد تعليمية
"""

import streamlit as st
import random
from datetime import datetime
import json
from pathlib import Path

class ResourcesLibrary:
    def __init__(self):
        self.resources = self.load_resources()
        self.daily_tips = self.load_daily_tips()
        self.articles = self.load_articles()
        self.emergency_contacts = self.load_emergency_contacts()
    
    def load_resources(self):
        """تحميل الموارد النفسية"""
        return {
            "anxiety": {
                "title": "التعامل مع القلق",
                "icon": "😰",
                "color": "#FF9800",
                "tips": [
                    "تمرن على التنفس العميق لمدة 5 دقائق يومياً",
                    "اكتب مخاوفك على الورق لتقليل تأثيرها النفسي",
                    "مارس الرياضة بانتظام لتقليل هرمونات التوتر",
                    "تجنب الكافيين الزائد خاصة في المساء",
                    "حدد وقتاً محدداً للقلق (15 دقيقة يومياً فقط)",
                    "استخدم تقنية 5-4-3-2-1 للتركيز على اللحظة الحالية"
                ],
                "techniques": [
                    "تقنية التنفس 4-7-8",
                    "تمرين استرخاء العضلات التدريجي",
                    "تقنية إعادة التأطير المعرفي",
                    "تمرين اليقظة الذهنية"
                ],
                "when_to_seek_help": [
                    "عندما يؤثر القلق على عملك أو دراستك",
                    "إذا كنت تتجنب الأنشطة بسبب القلق",
                    "عند وجود أعراض جسدية مستمرة",
                    "إذا كان القلق يؤثر على علاقاتك"
                ]
            },
            "depression": {
                "title": "التعامل مع الاكتئاب",
                "icon": "😢",
                "color": "#9C27B0",
                "tips": [
                    "حافظ على روتين يومي ثابت",
                    "اخرج في الشمس لمدة 15 دقيقة يومياً",
                    "تواصل مع الأصدقاء والعائلة بانتظام",
                    "مارس أنشطة تستمتع بها حتى لو لم تشعر بالرغبة",
                    "اكتب يومياً 3 أشياء تشعر بالامتنان لها",
                    "تجنب اتخاذ قرارات مهمة أثناء نوبات الحزن"
                ],
                "techniques": [
                    "العلاج السلوكي المعرفي الذاتي",
                    "تمارين الامتنان اليومية",
                    "النشاط الجسدي المنتظم",
                    "تقنيات حل المشكلات"
                ],
                "when_to_seek_help": [
                    "عند فقدان الاهتمام بالأنشطة لأكثر من أسبوعين",
                    "إذا كانت لديك أفكار إيذاء النفس",
                    "عند تغيرات كبيرة في النوم أو الشهية",
                    "إذا كنت تشعر باليأس المستمر"
                ]
            },
            "stress": {
                "title": "إدارة الضغط النفسي",
                "icon": "😫",
                "color": "#FF5722",
                "tips": [
                    "نظم أولوياتك واكتب قائمة مهام يومية",
                    "تعلم قول 'لا' للالتزامات الإضافية",
                    "خذ فترات راحة قصيرة كل ساعة",
                    "مارس تمارين الاسترخاء قبل النوم",
                    "قسم المهام الكبيرة إلى خطوات صغيرة",
                    "احتفل بإنجازاتك الصغيرة"
                ],
                "techniques": [
                    "تقنية إدارة الوقت",
                    "تمارين الاسترخاء السريع",
                    "التفكير الإيجابي",
                    "تقنية حل المشكلات المنهجي"
                ],
                "when_to_seek_help": [
                    "عند الشعور بالإرهاق المستمر",
                    "إذا كان الضغط يؤثر على صحتك الجسدية",
                    "عند صعوبة في اتخاذ القرارات",
                    "إذا كنت تلجأ لعادات ضارة للتأقلم"
                ]
            },
            "general": {
                "title": "الصحة النفسية العامة",
                "icon": "🧠",
                "color": "#4CAF50",
                "tips": [
                    "احصل على 7-8 ساعات نوم يومياً",
                    "تناول وجبات متوازنة في أوقات منتظمة",
                    "مارس الرياضة لمدة 30 دقيقة يومياً",
                    "خصص وقتاً للهوايات والأنشطة الممتعة",
                    "تعلم مهارات جديدة لتحفيز عقلك",
                    "حافظ على علاقات اجتماعية صحية"
                ],
                "techniques": [
                    "تقنيات اليقظة الذهنية",
                    "التأمل اليومي",
                    "كتابة اليوميات",
                    "التطوع ومساعدة الآخرين"
                ],
                "when_to_seek_help": [
                    "عند الشعور بالحاجة للدعم الإضافي",
                    "للوقاية والحفاظ على الصحة النفسية",
                    "عند مواجهة تغيرات كبيرة في الحياة",
                    "للتطوير الشخصي والنمو"
                ]
            }
        }
    
    def load_daily_tips(self):
        """تحميل النصائح اليومية"""
        return [
            {
                "tip": "ابدأ يومك بـ 5 دقائق تأمل أو تنفس عميق",
                "category": "morning",
                "icon": "🌅"
            },
            {
                "tip": "اشرب كوب ماء فور استيقاظك لتنشيط جسمك",
                "category": "health",
                "icon": "💧"
            },
            {
                "tip": "اكتب 3 أشياء تشعر بالامتنان لها كل مساء",
                "category": "gratitude",
                "icon": "🙏"
            },
            {
                "tip": "خذ استراحة من الشاشات كل ساعة لمدة 5 دقائق",
                "category": "digital_wellness",
                "icon": "📱"
            },
            {
                "tip": "تحدث مع صديق أو أحد أفراد العائلة اليوم",
                "category": "social",
                "icon": "👥"
            },
            {
                "tip": "امش في الطبيعة أو اجلس في مكان أخضر لمدة 10 دقائق",
                "category": "nature",
                "icon": "🌳"
            },
            {
                "tip": "اقرأ شيئاً إيجابياً أو ملهماً لمدة 15 دقيقة",
                "category": "learning",
                "icon": "📚"
            },
            {
                "tip": "مارس تمريناً بسيطاً أو تمدد لمدة 10 دقائق",
                "category": "exercise",
                "icon": "🏃"
            },
            {
                "tip": "استمع لموسيقى هادئة أو أصوات طبيعية",
                "category": "relaxation",
                "icon": "🎵"
            },
            {
                "tip": "نظف أو رتب مساحة صغيرة حولك",
                "category": "environment",
                "icon": "🧹"
            }
        ]
    
    def load_articles(self):
        """تحميل المقالات التعليمية"""
        return [
            {
                "title": "فهم القلق: الأسباب والحلول",
                "summary": "دليل شامل لفهم القلق وكيفية التعامل معه بطرق علمية مثبتة",
                "content": """
                القلق هو استجابة طبيعية للضغط، لكنه يصبح مشكلة عندما يؤثر على حياتك اليومية.
                
                ## أسباب القلق:
                - الضغوط الحياتية
                - العوامل الوراثية
                - التغيرات الهرمونية
                - استهلاك الكافيين المفرط
                
                ## علامات القلق:
                - سرعة ضربات القلب
                - التعرق
                - صعوبة التركيز
                - الأرق
                
                ## استراتيجيات التأقلم:
                1. **التنفس العميق**: مارس تقنية 4-7-8
                2. **التمرين**: 30 دقيقة يومياً
                3. **النوم الجيد**: 7-8 ساعات ليلاً
                4. **التغذية المتوازنة**: تجنب السكر والكافيين الزائد
                """,
                "category": "anxiety",
                "read_time": 5,
                "author": "فريق الصحة النفسية"
            },
            {
                "title": "بناء المرونة النفسية",
                "summary": "كيف تطور قدرتك على التعافي من الصعوبات والتحديات",
                "content": """
                المرونة النفسية هي القدرة على التكيف والتعافي من الصعوبات.
                
                ## خصائص الأشخاص المرنين:
                - يرون التحديات كفرص للنمو
                - يحافظون على نظرة إيجابية
                - يطلبون المساعدة عند الحاجة
                - يتعلمون من التجارب
                
                ## كيف تبني المرونة:
                1. **طور شبكة دعم قوية**
                2. **مارس الرعاية الذاتية**
                3. **ضع أهدافاً واقعية**
                4. **تعلم من الفشل**
                5. **حافظ على المنظور الإيجابي**
                """,
                "category": "general",
                "read_time": 7,
                "author": "د. أحمد محمد"
            }
        ]
    
    def load_emergency_contacts(self):
        """تحميل جهات الاتصال الطارئة"""
        return {
            "egypt": [
                {
                    "name": "الخط الساخن للصحة النفسية",
                    "number": "08008880700",
                    "description": "خدمة مجانية 24/7 للدعم النفسي",
                    "type": "hotline"
                },
                {
                    "name": "خط نجدة الطوارئ",
                    "number": "123",
                    "description": "للحالات الطارئة",
                    "type": "emergency"
                },
                {
                    "name": "مستشفى الصحة النفسية",
                    "number": "0227940000",
                    "description": "مستشفى العباسية للصحة النفسية",
                    "type": "hospital"
                }
            ],
            "international": [
                {
                    "name": "International Association for Suicide Prevention",
                    "website": "https://www.iasp.info/resources/Crisis_Centres/",
                    "description": "قائمة مراكز الأزمات عالمياً",
                    "type": "website"
                }
            ]
        }
    
    def get_daily_tip(self):
        """الحصول على نصيحة اليوم"""
        today_seed = int(datetime.now().strftime("%Y%m%d"))
        random.seed(today_seed)
        return random.choice(self.daily_tips)
    
    def get_tips_by_emotion(self, emotion):
        """الحصول على نصائح حسب الحالة النفسية"""
        if emotion in self.resources:
            return self.resources[emotion]
        return self.resources["general"]
    
    def search_resources(self, query):
        """البحث في الموارد"""
        results = []
        query_lower = query.lower()
        
        # البحث في النصائح
        for category, resource in self.resources.items():
            if query_lower in resource["title"].lower():
                results.append({
                    "type": "resource",
                    "category": category,
                    "data": resource
                })
        
        # البحث في المقالات
        for article in self.articles:
            if (query_lower in article["title"].lower() or 
                query_lower in article["summary"].lower()):
                results.append({
                    "type": "article",
                    "data": article
                })
        
        return results
    
    def get_personalized_recommendations(self, user_emotions_history):
        """الحصول على توصيات مخصصة بناءً على تاريخ المشاعر"""
        if not user_emotions_history:
            return self.resources["general"]
        
        # تحليل أكثر المشاعر تكراراً
        emotion_counts = {}
        for emotion in user_emotions_history:
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        most_common_emotion = max(emotion_counts, key=emotion_counts.get)
        return self.get_tips_by_emotion(most_common_emotion)


def display_daily_tip():
    """عرض نصيحة اليوم"""
    library = ResourcesLibrary()
    tip = library.get_daily_tip()
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                padding: 1.5rem; border-radius: 15px; color: white; margin: 1rem 0;'>
        <h3>{tip['icon']} نصيحة اليوم</h3>
        <p style='font-size: 1.1rem; margin: 0;'>{tip['tip']}</p>
    </div>
    """, unsafe_allow_html=True)


def display_resources_by_emotion(emotion):
    """عرض الموارد حسب الحالة النفسية"""
    library = ResourcesLibrary()
    resources = library.get_tips_by_emotion(emotion)
    
    st.markdown(f"""
    <div style='background: {resources["color"]}; color: white; padding: 2rem; 
                border-radius: 15px; text-align: center; margin: 1rem 0;'>
        <h2>{resources["icon"]} {resources["title"]}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # النصائح
    st.subheader("💡 نصائح مفيدة")
    for i, tip in enumerate(resources["tips"], 1):
        st.write(f"{i}. {tip}")
    
    # التقنيات
    st.subheader("🛠️ تقنيات مساعدة")
    for technique in resources["techniques"]:
        st.info(f"• {technique}")
    
    # متى تطلب المساعدة
    st.subheader("🚨 متى تطلب المساعدة المتخصصة")
    for sign in resources["when_to_seek_help"]:
        st.warning(f"• {sign}")


def display_emergency_contacts():
    """عرض جهات الاتصال الطارئة"""
    library = ResourcesLibrary()
    contacts = library.emergency_contacts
    
    st.header("🚨 جهات الاتصال الطارئة")
    
    st.subheader("🇪🇬 مصر")
    for contact in contacts["egypt"]:
        if contact["type"] == "hotline":
            st.success(f"📞 **{contact['name']}**: {contact['number']}\n{contact['description']}")
        elif contact["type"] == "emergency":
            st.error(f"🚨 **{contact['name']}**: {contact['number']}\n{contact['description']}")
        else:
            st.info(f"🏥 **{contact['name']}**: {contact['number']}\n{contact['description']}")
    
    st.subheader("🌍 دولي")
    for contact in contacts["international"]:
        st.info(f"🌐 **{contact['name']}**: {contact['website']}\n{contact['description']}")


def display_articles_library():
    """عرض مكتبة المقالات"""
    library = ResourcesLibrary()
    
    st.header("📚 مكتبة المقالات")
    
    for article in library.articles:
        with st.expander(f"📖 {article['title']} - {article['read_time']} دقائق قراءة"):
            st.write(f"**الملخص:** {article['summary']}")
            st.write(f"**الكاتب:** {article['author']}")
            st.markdown("---")
            st.markdown(article['content'])


def display_resources_library():
    """عرض مكتبة الموارد الكاملة"""
    st.header("📚 مكتبة الموارد النفسية")
    
    # نصيحة اليوم
    display_daily_tip()
    
    # البحث
    st.subheader("🔍 البحث في الموارد")
    search_query = st.text_input("ابحث عن موضوع معين...")
    
    if search_query:
        library = ResourcesLibrary()
        results = library.search_resources(search_query)
        
        if results:
            st.write(f"تم العثور على {len(results)} نتيجة:")
            for result in results:
                if result["type"] == "resource":
                    st.info(f"📋 {result['data']['title']}")
                elif result["type"] == "article":
                    st.info(f"📖 {result['data']['title']}")
        else:
            st.warning("لم يتم العثور على نتائج. جرب كلمات مختلفة.")
    
    # التبويبات
    tab1, tab2, tab3, tab4 = st.tabs(["😰 القلق", "😢 الاكتئاب", "😫 الضغط", "🧠 عام"])
    
    with tab1:
        display_resources_by_emotion("anxiety")
    
    with tab2:
        display_resources_by_emotion("depression")
    
    with tab3:
        display_resources_by_emotion("stress")
    
    with tab4:
        display_resources_by_emotion("general")
    
    # المقالات
    st.markdown("---")
    display_articles_library()
    
    # جهات الاتصال الطارئة
    st.markdown("---")
    display_emergency_contacts()


if __name__ == "__main__":
    # اختبار المكتبة
    library = ResourcesLibrary()
    
    # اختبار نصيحة اليوم
    tip = library.get_daily_tip()
    print(f"نصيحة اليوم: {tip['tip']}")
    
    # اختبار البحث
    results = library.search_resources("قلق")
    print(f"نتائج البحث: {len(results)}")
    
    print("تم تحميل مكتبة الموارد بنجاح!")


