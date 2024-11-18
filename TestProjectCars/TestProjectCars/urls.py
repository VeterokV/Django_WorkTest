from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('api/APIView/', SpectacularAPIView.as_view(), name='APIView'),                                                 # Генерация API схемы
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='APIView'), name='swagger-ui'),
    path('', include('cars.urls'))
]
