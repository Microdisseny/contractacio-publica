DEBUG = True

SECRET_KEY = '13p5$sz7_4g-a2^e$5=e&hxz$b=c6dr-beml*ubcwpc(u5ixe%'

AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
APP_URL = '/'
ALLOWED_HOSTS = ['*']
SPATIALITE_LIBRARY_PATH= 'mod_spatialite.so'