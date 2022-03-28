from django.urls import path

from . import views


urlpatterns = [
    path('v1/post/new/', views.NewPostView.as_view()),
    path('v1/post/<str:city>/', views.PostByCityView.as_view()),
]
