from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories' # admin에서 categorys 수정


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()



    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True) # 이 항목은 꼭 채우지 않아도 된다 

    created = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL) 

    def __str__(self): # 객체를 문자로 바꿨을때 어떻게 표현해야하는지 나타내주는 함수
        return '{} :: {}.'.format(self.title, self.author) #title, author 나오게

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)



