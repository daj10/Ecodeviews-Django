from django.contrib import admin
from django.urls import path, include

# for uploading image
from django.conf import settings
from django.conf.urls.static import static

#from blog.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('blog.urls')),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)