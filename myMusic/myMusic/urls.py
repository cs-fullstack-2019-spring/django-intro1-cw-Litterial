"""myMusic URL Configuration

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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('myArtist.urls')),
    path('music/',include('myArtist.urls')),
    path('music/Project Pat/',include('myArtist.urls')),
    path('music/TommyWright III/',include('myArtist.urls')),
    path('music/Three 6 Mafia/',include('myArtist.urls')),
    path('admin/', admin.site.urls),

]
