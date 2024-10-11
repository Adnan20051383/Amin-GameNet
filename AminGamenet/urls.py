"""
URL configuration for AminGamenet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import RedirectView

import authy

urlpatterns = [
    path('', RedirectView.as_view(url='/users/sign-in/', permanent=True)),
    path('admin/', admin.site.urls),
    path('users/', include('authy.urls')),
    path('home/', authy.views.home, name='home'),
    path('reserve/', authy.views.reserve_page, name='reserve'),
    path('reserve_table_form/<int:table_number>', authy.views.reserve_form, name='reserve_form'),
    path('release_table_form/<int:reserve_id>', authy.views.release_form, name='release_form'),
    path('history', authy.views.history, name='history'),
    path('add-snack/<int:reserve_id>', authy.views.add_snack, name='add-snack'),
    path('addSnack/<int:snack_id>/<int:reserve_id>/', authy.views.snackAdd, name='addSnack'),
    path('deleteSnack/<int:snack_id>/<int:reserve_id>/', authy.views.snackDelete, name='deleteSnack'),
]
