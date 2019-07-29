"""CarMarket URL Configuration

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
from CarMarket_app import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name ='home'),
    path('add/', views.add, name = 'add'),
    path('contact/', views.contact, name = 'contact'),
    path('details/<int:pk>',views.detailes, name = 'detailes'),
    path('login/',views.user_login, name = 'login'),
    path('market/',views.market, name = 'market'),
    path('register/',views.register, name = 'register'),
    path('logout/', views.user_logout, name='logout'),
    path('car/<int:pk>/update/', views.CarUpdate.as_view(), name='update-car'),
    path('car/<int:pk>/delete/', views.CarDelete.as_view(), name='delete-car'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
