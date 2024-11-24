from pathlib import Path
import os

from dotenv import load_dotenv
import os

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '63.176.250.78'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'refPrint'),
        'USER': os.getenv('DATABASE_USER', 'ilya'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'devZhyrgal006'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}

STATIC_URL = '/static/'
#STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATIC_ROOT = '/var/www/html/static'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
#	'/var/www/html/static',
]

MEDIA_URL = '/media/'
#MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_ROOT = '/var/www/html/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'zt20061113@gmail.com')  
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'kgyeeiwxktjurnne')  
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'zt20061113@gmail.com')
