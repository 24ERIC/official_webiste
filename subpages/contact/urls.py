from django.urls import path
from subpages.contact.views import index

urlpatterns = [
    path('', index),  # New Page path
]