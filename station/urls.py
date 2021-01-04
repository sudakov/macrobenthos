import django.contrib.auth.urls
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import StationCreateView, StationListView

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('<int:station_id>/', views.detail, name='detail'),
    path('station/new/', StationCreateView.as_view(), name='station_new'),
    path('station/list/', StationListView.as_view(), name='station-list'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view())
]
