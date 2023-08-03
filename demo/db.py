# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'demo',
#     'USER': 'kaviarasanmani',
#     'PASSWORD': 'TzyWQm71egIB',
#     'HOST': 'ep-wild-dust-69961560-pooler.ap-southeast-1.aws.neon.tech/demo',
    
#     'PORT': '5432',
    
#   }
# }


# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demo',
        'USER': 'test',
        'PASSWORD': '9Ke0JMPkvaqm',
        'HOST': 'ep-wild-dust-69961560.ap-southeast-1.aws.neon.tech',
        'PORT': '',  # Use an empty string to connect on the default port 5432
        'OPTIONS': {
            'sslmode': 'require',
            'options': 'endpoint=ep-wild-dust-69961560',
        },
    }
}
