from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/', include('app_sorting.urls')),
    path('', include('app_frontend.urls')),
]

