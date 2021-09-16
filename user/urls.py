from django.urls import path
from django.conf import settings
from .views import *

from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index')
]