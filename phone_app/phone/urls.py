from django.urls import path

from . import views

urlpatterns = [
    path('phone', views.index, name='index'),
    path('phone_form', views.get_phone, name='phone_form'),
    path('table', views.get_data, name='phone_table')
    
]