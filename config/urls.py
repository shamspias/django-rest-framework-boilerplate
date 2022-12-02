from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from simple_nlp_app.urls import simple_app_router

schema_view = get_schema_view(
    openapi.Info(
        title="API Title",
        default_version='v1',
        description="API for BoilerPlate",
        terms_of_service="https://github.com/shamspias",
        contact=openapi.Contact(email="shamsuddinpias0@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

router = DefaultRouter()
router.registry.extend(simple_app_router.registry)

urlpatterns = [
                  # admin panel
                  path('admin/', admin.site.urls),

                  # api
                  path('api/v1/', include(router.urls)),

                  # auth
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # swagger docs
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
