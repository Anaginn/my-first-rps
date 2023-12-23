from pathlib import Path


# Пути сборки внутри проекта выглядят следующим образом: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Быстрые настройки для разработки - непригодны для производства
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: храните секретный ключ, используемый в производстве, в тайне!
SECRET_KEY = 'django-insecure-uor8j*z1r%oyb69^gsetqe=f@xhf5oqmf#=_zt+ncr60v-k875'

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: не запускайте отладку в производстве!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


# Определение приложения

# Список строк, обозначающих все приложения, включенные в этом Установка Django.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'massiv',
]

# Активацмя списка промежуточного ПО для использования
#П ромежуточное ПО - это фреймворк хуков для обработки запросов/ответов Django.
# Это легкая, низкоуровневая система "плагинов" для глобального изменения ввода Django или вывода.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Строка, представляющая полный путь импорта Python к корневому URLconf
ROOT_URLCONF = 'mysite.urls'

# Список, содержащий настройки для всех шаблонизаторов,
# с которыми будут использоваться Джанго. Каждый элемент списка представляет собой словарь,
# содержащий параметры для Индивидуальный двигатель.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# бд
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Используемая серверная часть базы данных. Встроенные бэкенды баз данных
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Проверка попроля
# Список валидаторов, которые используются для проверки надежности паролей пользователей
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Интернационализация. Цель интернационализации и локализации состоит в том,
# чтобы создать единую сеть предлагать свой контент на языках и в форматах, адаптированных к публика.
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
