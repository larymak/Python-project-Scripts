from django.urls import re_path
from room.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/rooms/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
]