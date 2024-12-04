from django.urls import path
from . import views

urlpatterns=[
    path('',views.cloud_login),
    path('register',views.register),
    path('cloud_home',views.cloud_home),
    path('cloud_logout',views.cloud_logout),
]