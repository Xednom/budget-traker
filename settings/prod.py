from .base import * 

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com', '.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dacb2mrpfbj0an',
        'USER': 'xascfmypogaajd ',
        'PASSWORD': 'c62aa9b963403fe109eaf936b4cb2b133f6fc18fe77de44b17f16c7bd31dfec0',
        'HOST': 'ec2-34-232-147-86.compute-1.amazonaws.com',
        'PORT': '5432',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'mabtracker$budget',
        # 'USER': 'mabtracker',
        # 'PASSWORD': 'fishmond22',
        # 'HOST': 'mabtracker.mysql.pythonanywhere-services.com',
        # 'PORT': '3306',
        # 'OPTIONS': {
        #  'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        # },
    }
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'formatters': {
		'django.server': {
			'()': 'django.utils.log.ServerFormatter',
			'format': '[%(server_time)s] %(asctime)s %(message)s',
		}
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
		},
		'console_debug_false': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'logging.StreamHandler',
		},
		'django.server': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'django.server',
		},
		# 'mail_admins': {
		# 	'level': 'ERROR',
		# 	'filters': ['require_debug_false'],
		# 	'class': 'django.utils.log.AdminEmailHandler'
		# }
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'console_debug_false'],
			'level': 'INFO',
		},
		'django.server': {
			'handlers': ['django.server'],
			'level': 'INFO',
			'propagate': False,
		}
	}
}

# see https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'frontend/dist')
)

# SSL/TLS SETTINGS FOR DJANGO
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = True
SECURE_HSTS_SECONDS = 1000000
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'



# DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)