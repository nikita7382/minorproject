from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mylist/',views.my_list,name='mylist'),
    path('recommend/',views.recommend,name='recommend'),
    path('register/',views.register,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),

]
