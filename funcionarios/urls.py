"""
URL configuration for funcionarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from contatos.views import index, detalhar, FuncionarioViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

routers = routers.SimpleRouter()
routers.register("funcionarios", FuncionarioViewSet, basename="funcionarios")

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("detalhar/<int:id>", detalhar, name="detalhar"),
    path("api/", include(routers.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
