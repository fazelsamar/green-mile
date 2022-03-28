from django.urls import path

from . import views


urlpatterns = [
    path('v1/location/provinces/', views.ProvincesView.as_view()),
]
