from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_ajax/', views.form_ajax, name='form_ajax'),
    path('message_ajax/', views.message_ajax, name='message_ajax'),
]