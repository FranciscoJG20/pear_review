"""pear_review_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from pear_review_app import views as pear_views
from django.contrib.auth import views as auth_views


# ^^^ I am adding an import - include 
# so that I can include other url files in our main one. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pear_review_app.urls')),
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/logout/', auth_views.logout, name='logout'),
    path('accounts/signup/', pear_views.sign_up, name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# ^^^ I'm setting the default values for the LOGIN_URL, LOGOUT_URL and the LOGIN_REDIRECT_URL. 
# The LOGIN_REDIRECT_URL will be used to redirect the user after authenticating 
# from Django Login AND Social Auth.