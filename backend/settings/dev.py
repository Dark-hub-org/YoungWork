from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/static/webpack-stats.json'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "frontend/dist/img/media/")

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

VUE_ROOT = os.path.join(os.path.join(BASE_DIR, "frontend"), "dist")
