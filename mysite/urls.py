from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', include('home.urls')),
    path('about/', include('subpages.about.urls')),
    path('contact/', include('subpages.contact.urls')),
    path('events/', include('subpages.events.urls')),
    path('products/', include('subpages.products.urls')),
]




from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)