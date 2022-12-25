from django.urls import path
from subpages.events.views import index

urlpatterns = [
    path('', index),  # New Page path
]