from django.urls import path
from . import views

urlpatterns = [
    path('',views.roomview, name="room"),
    path('<slug:slug>', views.room_detail,name="roomdetail"),
    path('room/create',views.create, name="create")
]