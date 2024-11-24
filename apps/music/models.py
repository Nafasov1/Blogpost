from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Music/image')
    music = models.FileField(upload_to='Music/music')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title