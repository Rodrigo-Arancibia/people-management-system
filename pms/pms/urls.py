"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from addresses.views import detail_address, new_address, edit_address, delete_address
from people.views import detail_person, new_person, edit_person, delete_person
from webapp.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='index'),

    path('detail_person/<int:id>', detail_person),
    path('new_person/', new_person),
    path('edit_person/<int:id>', edit_person),
    path('delete_person/<int:id>', delete_person),

    path('new_address/', new_address),
    path('detail_address/<int:id>', detail_address),
    path('edit_address/<int:id>', edit_address),
    path('delete_address/<int:id>', delete_address),
]