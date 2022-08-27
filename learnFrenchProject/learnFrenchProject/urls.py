"""learnFrenchProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from learnFrench.views import home, instruction_manual, register_request, login_request, logout_request, unit1, unit2, \
    lesson1, lesson2, profile, test1, test2

urlpatterns = [
    path('admin/', admin.site.urls),
path('home/', home, name="home"),
    path('instruction-manual/', instruction_manual, name="instruction_manual"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
    path("unit1/", unit1, name="unit1"),
    path("unit2/", unit2, name="unit2"),
    path("lesson1/", lesson1, name="lesson1"),
    path("lesson2/", lesson2, name="lesson2"),
    path("profile/", profile, name="profile"),
    path("test1/", test1, name="usertest"),
    path("test2/", test2, name="usertest")
]