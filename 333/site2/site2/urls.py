"""
site2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from sofar import views
#from django.urls import include, path, re_path
from django.urls import path, re_path

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path("", views.index),
    path('admin/', admin.site.urls),
    path('sofar/', views.postsofar), 
    re_path(r'sofarid+', views.getdatasofar),
    #re_path(r'sofarid+', modul1.getdatasofar),
    
    #re_path(r'?ID=\d+&name=tp', modul1.getdatasofar),
    #path('index?id=\d+/', views.getdatasofar),
         #include('sofar.urls')),kwargs=
    
]
