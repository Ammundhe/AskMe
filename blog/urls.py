from django.urls import path
from . import views

urlpatterns = [
    path('post', views.BlogPost.as_view(), name="BlogPost"),
    path('post/<str:slug>', views.Post.as_view(), name="Post"),
]
