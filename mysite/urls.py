from django.contrib import admin
from django.urls import path, include





from subpages.posts.views import home, post, events


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('about/', include('subpages.about.urls')),
    path('contact/', include('subpages.contact.urls')),
    path('products/', include('subpages.products.urls')),
    path('', home, name = 'home'),
    path('post/<slug>/', post, name = 'post'),
    path('events/', events, name = 'allposts'),
    path('tinymce/', include('tinymce.urls'))
]





from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

