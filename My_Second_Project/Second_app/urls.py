from django.conf.urls import url
from django.urls import path
from Second_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form')
]
