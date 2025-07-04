"""
URL configuration for lliga project.

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

from futbol import views

urlpatterns = [
    #auth routes
    path("accounts/", include("django.contrib.auth.urls")),
    #path("accounts/profile/", profile, name="profile"),

    #admin
    path('admin/', admin.site.urls),

    #front end
    path('classificacio', views.classificacio_menu),
    path('classificacio/<int:lliga_id>/', views.classificacio, name="classificacio"),
    path('crea_equip', views.crea_equip),
    path('prova_auth', views.prova_auth),
]
