from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import export_products_csv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('export/', export_products_csv, name='export_products_csv')

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

