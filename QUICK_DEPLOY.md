# 🚀 نشر سريع على Streamlit Cloud (5 دقائق)

## خطوات سريعة:

### 1️⃣ ارفع المشروع على GitHub
- اذهب إلى: https://github.com/new
- أنشئ مستودع جديد باسم: `AI-Mental-Health-Assistant`
- ارفع الملفات (استخدم GitHub Desktop أو Git)

### 2️⃣ انشر على Streamlit Cloud
- اذهب إلى: https://share.streamlit.io
- اضغط **Sign in with GitHub**
- اضغط **New app**
- اختر المستودع: `username/AI-Mental-Health-Assistant`
- **Main file**: `app.py`
- اضغط **Deploy!**

### 3️⃣ أضف مفتاح API (مهم!)
- بعد النشر، اضغط **⋮** → **Settings** → **Secrets**
- أضف:
  ```
  GEMINI_API_KEY = "مفتاحك هنا"
  ```
- اضغط **Save**

### 4️⃣ جاهز! 🎉
- ستحصل على رابط مثل: `https://your-app-name.streamlit.app`
- شارك الرابط مع أي شخص!

---

## ⚡ تحديث سريع:

```bash
git add .
git commit -m "Update"
git push
```
Streamlit Cloud سيحدث تلقائياً! ✨

---

📖 **للمزيد من التفاصيل**: اقرأ `DEPLOYMENT_GUIDE.md`
