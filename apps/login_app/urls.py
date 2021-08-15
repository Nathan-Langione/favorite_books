from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),   #dispaly all user
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),

]