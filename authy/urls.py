from django.urls import path
from django.contrib.auth import views as auth_views
from authy import views

urlpatterns = [
    path('sign-in/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),
]
