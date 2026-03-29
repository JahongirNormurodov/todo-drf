from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # yoki ['templates'] bo‘lishi mumkin
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',      # ✅ SHU QO‘SHILADI
                'django.contrib.messages.context_processors.messages',  # ✅ SHU HAM
            ],
        },
    },
]