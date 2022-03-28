from django.urls import path
from rest_framework.authtoken import views as rst

from . import views


urlpatterns = [
    path('api-token-auth/', rst.obtain_auth_token),
    path('v1/account/login/', views.LoginView.as_view()),
    path('v1/account/register/', views.RegisterView.as_view()),
]
