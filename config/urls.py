from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Blog
    path('api/v1/', include('posts.urls')),
    # Auth
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('dj_rest_auth.urls')),
    path('api/v1/register/', include('dj_rest_auth.registration.urls')),
    # Schema & Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
]
