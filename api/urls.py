from django.urls import path, include
from django.db import router
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('signup', views.signup)
router.register('question-category', views.questionCategoryview)
router.register('question', views.questionView)
router.register('blog-category', views.blogCategoryView)
router.register('blog-post', views.blogView)
router.register('answer', views.answerView)

urlpatterns = [
    path('login', views.LoginPage.as_view()),
    path('', include(router.urls)),
]
