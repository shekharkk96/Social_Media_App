from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(),name="all"),
    path('create/',views.CreateGroup.as_view(),name="create"),
    path('posts/in/<str:slug>/',views.SingleGroup.as_view(),name="single"),
    #difference between path and urls
    #https://consideratecode.com/2018/05/02/django-2-0-url-to-path-cheatsheet/#:~:text=In%20Django%202.0%2C%20you%20use,converters%20to%20capture%20URL%20parameters.&text=path()%20always%20matches%20the,is%20passed%20to%20a%20view.
    path('join/<str:slug>/',views.JoinGroup.as_view(),name="join"),
    path('leave/<str:slug>/',views.LeaveGroup.as_view(),name="leave"),
]
