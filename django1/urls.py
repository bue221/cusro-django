"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django2 import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/<str:nombre>', views.contacto , name='contacto'),
    path('contacto/', views.contacto , name='contacto'),
    path('articulo/<int:num>', views.articulo , name='articulo'),
    path('editar/<int:id>', views.editar , name='editar'),
    path('articulos/', views.articulos , name='articulos'),
    path('borrar/<int:id>', views.borrar , name='borrar'),
    path('save/', views.save , name='save'),
    path('create/', views.create , name='create'),
    path('create-art/', views.create_articulo , name='create_articulo'),
]

#configuracion imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



