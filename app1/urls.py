from django.urls import path
from app1.views import *
app_name='Mani'
urlpatterns=[
    path('sachin/',sachin,name='sachin'),
]