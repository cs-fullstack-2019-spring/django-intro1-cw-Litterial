#App url


from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('music/',views.music,name='index'),
    path('music/Project Pat/',views.ProP,name='index'),
    path('music/TommyWright III/',views.TW,name='index'),
    path('music/Three 6 Mafia/',views.Three6,name='index')
    ]