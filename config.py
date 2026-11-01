import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'development-only-change-me')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR / "instance" / "atelier_home.db"}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 110 * 1024 * 1024  # Supports a video upload plus images in one form
    MAX_PRODUCT_IMAGE_BYTES = 5 * 1024 * 1024
    MAX_PRODUCT_VIDEO_BYTES = 100 * 1024 * 1024
    MAX_PAYMENT_EVIDENCE_BYTES = 5 * 1024 * 1024
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV') == 'production'
    WTF_CSRF_TIME_LIMIT = None
    STORE_NAME = os.getenv('STORE_NAME', 'Atelier Home')
    STORE_CURRENCY = os.getenv('STORE_CURRENCY', 'USD')
    WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER', '447352794862')
    SUPPORT_EMAIL = os.getenv('SUPPORT_EMAIL', 'hello@example.com')
    ORDER_NOTIFY_EMAIL = os.getenv('ORDER_NOTIFY_EMAIL', '')
    SMTP_HOST = os.getenv('SMTP_HOST', '')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
    SMTP_FROM = os.getenv('SMTP_FROM', '')
    ORDER_NOTIFY_WHATSAPP = os.getenv('ORDER_NOTIFY_WHATSAPP', '')
    WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN', '')
    WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID', '')
    WHATSAPP_ORDER_TEMPLATE = os.getenv('WHATSAPP_ORDER_TEMPLATE', '')
    WHATSAPP_TEMPLATE_LANGUAGE = os.getenv('WHATSAPP_TEMPLATE_LANGUAGE', 'en_US')
    UPLOAD_FOLDER = str(BASE_DIR / 'uploads' / 'payment_evidence')
    PRODUCT_UPLOAD_FOLDER = str(BASE_DIR / 'uploads' / 'products')
