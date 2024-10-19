from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),  # Home page URL
    path("<str:room>/", views.room, name="room"),  # Room page with dynamic room name
    path("checkview", views.checkview, name="checkview"),  # For checking and creating rooms
    path("send", views.send, name="send"),  # Sending messages
    path("getMessages/<str:room>/", views.getMessages, name="getMessages"),  # Fetching messages for a specific room

]
