from django.db import models
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    quote = models.TextField(blank=True,null=True)
    published = models.DateTimeField(null=True,blank=True,default=now())


    def publish(self):
        self.published = now()
        self.save()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('news:details',kwargs={'pk':self.pk})

class EmailUs(models.Model):
    name = models.CharField(max_length=240)
    tel = models.CharField(max_length=240)
    email = models.EmailField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.name
class Images(models.Model):
    post = models.ForeignKey(News,default=None,on_delete=True)
    pic = models.ImageField(upload_to='post_pic', blank=True)
    video = models.FileField(upload_to='post_vid', blank=True)