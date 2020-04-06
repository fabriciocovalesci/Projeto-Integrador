"""backend URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

from rest_framework import routers

from backend.usuario.api.viewsets import UsuarioViewSets
from backend.cafes.api.viewsets import CafesViewSets
from backend.doces.api.viewsets import DocesViewSets
from backend.salgados.api.viewsets import SalgadosViewSets


"""
Rotas dos endpoints da API
"""
router = routers.DefaultRouter()
router.register(r'api/v1/usuario', UsuarioViewSets)
router.register(r'api/v1/cafes', CafesViewSets)
router.register(r'api/v1/doces', DocesViewSets)
router.register(r'api/v1/salgados', SalgadosViewSets)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
