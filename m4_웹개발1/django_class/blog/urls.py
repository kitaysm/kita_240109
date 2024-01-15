from django.urls import path
from . import views

# urlpatterns = [
#     path('<int:pk>/', views.single_post_page), # pk가 정수형임을 명시
#     path('', views.index), # 블로그 메인 페이지
# ]

urlpatterns = [
    path("search/<str:q>/", views.PostSearch.as_view()), # search에 쿼리가 들어오면 url에 반영
    path("delete_comment/<int:pk>/", views.delete_comment),
    path("update_comment/<int:pk>/", views.CommentUpdate.as_view()),
    path("update_post/<int:pk>/", views.PostUpdate.as_view()),
    path("create_post/", views.PostCreate.as_view()),
    path("tag/<str:slug>/", views.tag_page),
    path("category/<str:slug>/", views.category_page),
    path("<int:pk>/new_comment/", views.new_comment),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("", views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]