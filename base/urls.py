from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('selectRoom', views.select_room, name="selectRoom"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
]