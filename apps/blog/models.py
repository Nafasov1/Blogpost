from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/images/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Description(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='descriptions')
    checbok = models.BooleanField(default=False)
    description = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


