Step1: Setting Up the Backend with Django
1.1 Install Django and Create New Project
    pip install django djangorestframework channels
    django-admin startproject Zentra
    cd Zentra
1.2 Create a New App
    python manage.py startapp polls
1.3 configure Settings
    'Zentra/settings.py'
1.4 Set Up Database Apply initial migrations and create a superuser
    python manage.py migrate
    python manage.py createsuperuser
1.5 Create User Models
    User, interest and Message models
1.6 Create Serializers and views
    polls/serialization.py
    polls/views.py
1.7 configure URLs
    polls/urls.py
    Zentra/urls.py
1.8 Set Up Channels configure ASGI for webScoket support:
    Zentra/asgi.py
1.8 Cerate a consumer in polls/consumers.py

