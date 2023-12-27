from django.urls import path
from . import views

urlpatterns = [
    path('myApp/', views.myApp, name='myApp'),

]