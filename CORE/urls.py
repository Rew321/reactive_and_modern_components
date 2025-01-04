
from django.contrib import admin
from django.urls import path, include
import django_unicorn

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("unicorn/", include("django_unicorn.urls")),
    
    path('', include('ModernComponents.urls')),
]
