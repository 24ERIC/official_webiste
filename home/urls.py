from django.urls import path
from home.views import index

urlpatterns = [
    path('', index),  # New Page path
]