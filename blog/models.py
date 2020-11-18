from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True) # 이 항목은 꼭 채우지 않아도 된다 

    created = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager() 

    def __str__(self): # 객체를 문자로 바꿨을때 어떻게 표현해야하는지 나타내주는 함수
        return '{} :: {}.'.format(self.title, self.author) #title, author 나오게
