from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginPage.as_view(), name="LoginPage"),
    path('logout', views.LogoutPage, name="LogoutPage"),
    path('create-account', views.CreateAccount.as_view(), name="CreateAccount"),
    path('update-profile', views.updateProfile.as_view(), name="updateProfile")
]
