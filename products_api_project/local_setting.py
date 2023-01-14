# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l@e-h(fwnrw=hg1p4l4oy()dsa*0j)1^aq3kox6#^-*%@m9sma'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'imcoder82'
    }
}