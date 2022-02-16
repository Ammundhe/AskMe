from re import search
from django.shortcuts import render
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from answer.models import answer
from .serializers import userSerializer, questcategorySerializer, questionSerializer, PostCategorySerializer, blogSerializer, answerSerializer
from django.contrib.auth.models import User
from question.models import question, questionCategory
from blog.models import PostCategory, blog



class LoginPage(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class signup(ModelViewSet):
    serializer_class=userSerializer
    queryset=User.objects.all()

class questionCategoryview(ModelViewSet):
    serializer_class=questcategorySerializer
    queryset=questionCategory.objects.all()

class questionView(ModelViewSet):
    authentication_classes=(TokenAuthentication, )
    permission_classes=[IsAuthenticated,]
    filter_backends=(filters.SearchFilter, filters.OrderingFilter,)
    search_fields=('question',)
    ordering_fields=('id',)
    serializer_class=questionSerializer
    queryset=question.objects.all()

class blogCategoryView(ModelViewSet):
    serializer_class=PostCategorySerializer
    queryset=PostCategory.objects.all()

class blogView(ModelViewSet):
    serializer_class=blogSerializer
    queryset=blog.objects.all()

class answerView(ModelViewSet):
    serializer_class=answerSerializer
    queryset=answer.objects.all()

