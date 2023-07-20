from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('userpage/', views.userpage, name='userpage'),
    path('signup', views.signup, name='signup'),
    path('parametro/<slug:data>/', views.parametro, name="parametro"),
]
