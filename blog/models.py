from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager() 

    def __str__(self): # 객체를 문자로 바꿨을때 어떻게 표현해야하는지 나타내주는 함수
        return '{} :: {}.'.format(self.title, self.author) #title, author 나오게
