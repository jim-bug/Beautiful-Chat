"""
URL configuration for bc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, re_path
from . import consumers
from beautiful_chat import views
=======
from django.urls import path

from beautiful_chat import views, profile
>>>>>>> d213a0e43bb7044791e08e054b177669b168bc81



websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chats/', views.chats),
    path('chats/create/', views.new_chat),
    path('chats/<str:chat_id>/', views.chats),
<<<<<<< HEAD
    path('login/', views.loginRoute),
    path('logout/', views.logoutRoute),
    path('register/', views.register),
    path('', views.index),
    websocket_urlpatterns[0]

=======
    path('profile_picture/<str:hash>', profile.profile_picture),
    path('profile_picture/', profile.profile_picture),
    path('profile/', profile.view_profile),
    path('login/', profile.loginRoute),
    path('logout/', profile.logoutRoute),
    path('register/', profile.register),
    path('', views.index)
>>>>>>> d213a0e43bb7044791e08e054b177669b168bc81
]
