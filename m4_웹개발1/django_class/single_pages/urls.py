from django.urls import path
from . import views

urlpatterns = [
    # path('about_me/', views.about_me),
    path('about_me/', views.about_me),
    path('', views.landing),
]
# 아무것도 없으면 views의 랜딩
# about_me 써있으면 about_me로 이동.