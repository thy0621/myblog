from django.db import models

# Create your models here.
class Article(models.Model): # 修改记得在cmd里移植（migration+migrate）
    title=models.CharField(max_length=32,default='Title')
    content=models.TextField(null=True)
    pub_time=models.DateTimeField(null=True)

    def __str__(self):
        return self.title