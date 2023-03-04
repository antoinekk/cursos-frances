from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cursos_chihuahua/', include('cursos_app.urls')),
    path('admin/', admin.site.urls),
]
