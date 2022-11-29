from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_ajax/', views.form_ajax, name='form_ajax'),
    path('message_ajax/', views.message_ajax, name='message_ajax'),
    path('form_ajax2/', views.form_ajax2, name='form_ajax2'),
    path('message_ajax2/', views.message_ajax2, name='message_ajax2'),
    path('form_ajax3/', views.form_ajax3, name='form_ajax3'),
    path('message_ajax3/', views.message_ajax3, name='message_ajax3'),
]