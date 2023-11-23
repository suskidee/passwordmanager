from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('all/', views.view_all, name="all"),
    path('add/', views.add, name="add"),
    path('search/<str:my_search>/', views.search, name="search"),
    path('view/<int:pk>/', views.view, name="view"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('accounts/login/', views.login_user, name="login"),
]
