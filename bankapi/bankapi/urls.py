"""bankapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from api import views
from api.views import search_ifsc, home, about
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewsets with it.
# The API URLs are now determined automatically by the router.
router = DefaultRouter()
router.register('bankdetailapi', views.BankViewSet, basename='bankdetail' )
# router.register('searchbar', views.search_ifsc, basename='search')


urlpatterns = [
    path('index/' , home, name='home'),
    path('about/' , about, name='about'),
    path('admin/', admin.site.urls),
    path('api-root/', include((router.urls, 'api'), namespace='api-root')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ajax/search/' , views.search_ifsc, name='search_view')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
