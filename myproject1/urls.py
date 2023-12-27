from django.contrib import admin
from django.urls import include, path
from myApp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('courses/', courses, name='courses'),
    path('gallery/', gallery, name='gallery'),
    path('contacUs/', contacUs, name='contacUs'),
    path('login/', login, name='login'),

]
