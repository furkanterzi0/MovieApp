from django.urls import path
from . import views

urlpatterns = [
    path("login",views.AccountLogin,name="AccountLogin"),
    path("register",views.AccountRegister,name="AccountRegister"),
    path("logout",views.AccountLogout,name="AccountLogout")
]
