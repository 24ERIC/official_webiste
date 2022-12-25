from django.urls import path
from subpages.products.views import index

urlpatterns = [
    path('', index),  # New Page path
]