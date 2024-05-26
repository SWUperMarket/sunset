#my_settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'barom_db', #2
        'USER': 'root', #3                      
        'PASSWORD': '12345',  #4              
        'HOST': 'localhost',   #5                
        'PORT': '3306', #6
    }
}
