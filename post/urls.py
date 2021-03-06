from django.urls import path

from . import views


urlpatterns = [

    path('v1/posts/', views.PostList.as_view()),

    path('v1/post/<int:pk>/', views.PostRetrieve.as_view()),

    path('v1/post/new/', views.NewPostView.as_view()),

    path('v1/post/<int:post_id>/new-comment/', views.NewCommentView.as_view()),

    path('v1/post/<int:post_id>/like/', views.ToggleLikeView.as_view()),

    path('v1/post/by-province/<str:province>/',
         views.PostByProvinceView.as_view()),

    path('v1/post/<int:post_id>/new-welfare-place/',
         views.NewWelfarePlaceView.as_view()),

]
