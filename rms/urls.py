"""rms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="home"),
    path('materials/', material_view, name="materials"),
    path('main/', main, name="main"),
    path('create_course/', create_course, name="create_course"),
    path('create_student/', create_student, name="create_student"),
    path('manage_course/', manage_course, name="manage_course"),
    path('manage_department/', manage_department, name="manage_department"),
    path('manage_result/', manage_result, name="manage_result"),
    path('show_result/', show_results, name="show_result"),
    path('manage_student/', manage_student, name="manage_student"),
    path('manage_materials/', manage_materials, name="manage_materials"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
