from pathlib import Path
from urllib.parse import quote
from dotenv import load_dotenv
import os


load_dotenv()
KEY = os.getenv('KEY')

SECRET_KEY = KEY
ALLOWED_HOSTS = ['localhost','127.0.0.1','0.0.0.0', 'studyways.ir']

CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
DEBUG = os.getenv("DEBUG") == "True"
JWT_SECRET = os.getenv("JWT_SECRET", default=SECRET_KEY)

BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 2


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.sites",
)
THIRD_PARTY_APPS = (
    "rest_framework",
    "django_filters",
    "corsheaders",
    "gunicorn",
    "whitenoise",
)
LOCAL_APPS = (
    "accounts",
    "blog",
)


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]




# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"



# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "accounts.backends.JWTAuthentication",
        #"rest_framework.authentication.TokenAuthentication",
        #"rest_framework.authentication.SessionAuthentication",
        #"oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        #"drf_social_oauth2.authentication.SocialAuthentication",
    ),
    "DEFAULT_THROTTLE_RATES": {"otp": os.getenv("OTP_THROTTLE_RATE", default="10/min"), },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
# END REST FRAMEWORK CONFIGURATION



# CORSHEADERS CONFIGURATION
ALLOWED_HOSTS = ['studyways.ir','localhost','127.0.0.1','0.0.0.0', 'liara.run','app.studyways.ir']
CORS_ALLOWED_ORIGINS = ["https://app.studyways.ir","https://liara.run","http://localhost","http://127.0.0.1","https://studyways.ir","https://.liara.run","https://.studyways.ir"]
CSRF_TRUSTED_ORIGINS = ["https://app.studyways.ir","https://liara.run","http://localhost","http://127.0.0.1","https://studyways.ir","https://.liara.run","https://.studyways.ir"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SECURE=True
CORS_ORIGIN_WHITELIST = ["https://app.studyways.ir","https://liara.run","http://localhost","http://127.0.0.1","https://studyways.ir","https://.liara.run","https://.studyways.ir"]
# END CORSHEADERS CONFIGURATION


APPEND_SLASH = True
