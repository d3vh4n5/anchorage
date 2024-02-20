from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('redirector/<slug:avatar>/', views.redirector, name='redirector'),
    path('parametro/<slug:data>/', views.parametro, name="parametro"),

    #userpage
    path('userpage/', views.userpage, name='userpage'),
    path('userpage/nuevo', views.nuevoLink, name='nuevoLink'),
]
