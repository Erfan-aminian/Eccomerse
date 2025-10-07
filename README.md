# 🛒 E-Commerce Platform (Django)

یک فروشگاه اینترنتی ساده و قابل توسعه با استفاده از **Django**.این پروژه شامل امکانات پایه یک سیستم فروشگاه آنلاین از جمله ثبت‌نام کاربران، نمایش محصولات، افزودن به سبد خرید، پرداخت و مدیریت سفارش‌ها می‌باشد.
<p>Home page:</p>
<img width="1860" height="1080" alt="home page" src="https://github.com/user-attachments/assets/59d6c7a3-e2b1-4812-81ef-4f276d5d005d" />

<p>Product detail:</p>
<img width="1863" height="1080" alt="product" src="https://github.com/user-attachments/assets/6795a500-f766-44c3-9030-87fbd040ed8e" />

<p>Sign in:</p>
<img width="1866" height="1080" alt="sign in" src="https://github.com/user-attachments/assets/4ca12ff4-8a86-42e8-a2f7-99311f2778df" />

<p>Sign up:</p>
<img width="1863" height="1078" alt="sign up" src="https://github.com/user-attachments/assets/07fd484e-2f35-4b3c-84fb-bae54f9ca7cc" />

<p>Cart:</p>
<img width="1864" height="1080" alt="cart" src="https://github.com/user-attachments/assets/1b1f20dc-fa09-444e-bdae-69366177bd47" />

<p>Cart detail:</p>
<img width="1862" height="1080" alt="cart2" src="https://github.com/user-attachments/assets/d7964e22-57f7-4708-80e4-af517550c215" />

## 📌 ویژگی‌ها

- ثبت‌نام و ورود کاربران
- لیست محصولات به همراه جزئیات
- جستجو و فیلتر محصولات
- افزودن محصولات به سبد خرید
- ثبت سفارش و پیگیری وضعیت سفارش
- پنل مدیریت برای افزودن/ویرایش محصولات
- طراحی شده با استفاده از Django Template و , Js , Html & Css ,Bootstrap

## 🛠 تکنولوژی‌ها

- **Backend:** Django 4.x
- **Database:** SQLite (قابل تغییر به PostgreSQL)
- **Frontend:** HTML5, CSS3, Bootstrap
- **Auth:** Django built-in authentication

## 🚀 شروع سریع (لوکال)

### پیش‌نیازها

- Python 3.10 یا بالاتر
- pip
- virtualenv (اختیاری ولی توصیه‌شده)

### مراحل اجرا

```bash
# کلون کردن ریپو
git clone https://github.com/Erfan-aminian/E-Commerce.git
cd E-Commerce

# ساخت و فعال‌سازی محیط مجازی
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# مهاجرت دیتابیس
python manage.py migrate

# ساخت سوپر یوزر برای پنل ادمین
python manage.py createsuperuser

# اجرای سرور
python manage.py runserver
