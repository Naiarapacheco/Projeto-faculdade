from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('detail/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
