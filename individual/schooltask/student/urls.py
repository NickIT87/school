from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search', Search.as_view(), name='search'),
]