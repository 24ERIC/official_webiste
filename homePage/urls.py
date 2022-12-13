from django.urls import path
from homePage.views import index

urlpatterns = [
    path('', index),  # New Page path
]