from django.urls import path
from django.contrib.auth import views as auth_v
from . import views

app_name = 'all_accounts'

urlpatterns = [
    path('login/',auth_v.LoginView.as_view(template_name="all_accounts/login.html"),name="login"),
    path('logout/', auth_v.LogoutView.as_view(),name="logout"),
    path('signup/',views.SignUp.as_view(), name="signup"),
]
