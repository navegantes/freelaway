from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('jobs/', include('jobs.urls')),
    path('', views.encontrar_jobs)  # include('jobs.urls')),
]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
