from .base import *

env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env')) # BASE_DIR과 .env를 join하여 운영체제 상에서

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # 디버깅 관련 정보를 내보내지 않음

ALLOWED_HOSTS = ['*'] # 접속 가능한 호스트를 넣어 주는 곳, *: 모든 ip의 호스트를 넣어주는 것



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}