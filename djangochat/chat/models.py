from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)


class Messages(models.Model):
    value = models.TextField()
    user = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
