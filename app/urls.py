
from django.contrib import admin
from django.urls import path
from app.views import home,login,signup,add_todo,signout,delete_todo,change_todo


urlpatterns = [
    path('',home, name='home'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('add-todo/',add_todo, name = 'add_todo'),
    path('delete-todo/<int:id>',delete_todo, name = 'delete_todo'),
    path('change-status-todo/<int:id>/<str:status>',change_todo, name = 'change_todo'),
    path('logout/',signout)
]
