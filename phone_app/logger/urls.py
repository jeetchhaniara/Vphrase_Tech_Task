from django.urls import path

from . import views

urlpatterns = [
    path('logger', views.logger, name='logger'),
]