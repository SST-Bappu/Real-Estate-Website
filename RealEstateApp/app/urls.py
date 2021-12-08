from django.urls import path
from .views import *
urlpatterns = [
    path('reg/', registraion.as_view(),name='register'),
]