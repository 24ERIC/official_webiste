from django.urls import path
from subpages.about.views import index

urlpatterns = [
    path('', index),  # New Page path
]