"""jango URL Configuration

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
from django.urls import path,include
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('men/', views.men),
    path('women/', views.women),
    path('beauty/', views.Beauty),
    path('footwear/', views.footwear),
    path('z-world/', views.zworld),
    path('shop/', views.shop),
    path('kids/', views.kids),
    path('contact/', views.contact),
    path('result/',views.read),
    path('insert/',views.insert),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    
   
       
]
