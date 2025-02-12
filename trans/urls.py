from django.urls import path
from trans.views import *
from . import views

app_name = 'trans'

urlpatterns = [
    path('', views.index,name='index'),
    path('new', new, name='new'),
]
