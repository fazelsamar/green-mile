from django.urls import path

from . import views


urlpatterns = [
    path('v1/post/new/', views.NewPostView.as_view()),
    path('v1/post/<int:post_id>/new-comment/', views.NewCommentView.as_view()),
    path('v1/post/<int:post_id>/like/', views.NewLikeView.as_view()),
    path('v1/post/by-city/<str:city>/', views.PostByCityView.as_view()),
]
