from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('create/',views.create,name="create"),
    path('vote/<str:pk>',views.vote,name='vote'),
    path('profile/',views.userprofile,name="profile"),
    path('delete/<int:id>',views.delete,name="delete")
]