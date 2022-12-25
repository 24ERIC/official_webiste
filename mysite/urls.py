from django.contrib import admin
from django.urls import path, include





from subpages.posts.views import homepage, post, about, search, postlist, allposts


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    # path('', include('home.urls')),
    # path('about/', include('subpages.about.urls')),
    # path('contact/', include('subpages.contact.urls')),
    # path('events/', include('subpages.events.urls')),
    # path('products/', include('subpages.products.urls')),
    
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    path('posts/', allposts, name = 'allposts'),
    
]




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

