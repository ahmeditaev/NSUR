from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    text = RichTextUploadingField(default='')
    quote = models.TextField(blank=True,null=True)
    quoteAuthor = models.TextField(blank=True,default='')
    published = models.DateTimeField(null=True,blank=True,default=now())
    pic = models.ImageField(upload_to='post_pic', blank=True)
    video = models.FileField(upload_to='post_vid',blank=True)
    previewImage = models.ImageField(upload_to='preview_pic',blank = True)

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
class PressClipping(models.Model):
    new = models.OneToOneField(News,on_delete=models.CASCADE)

    def __str__(self):
        return self.new
    def get_absolute_url(self):
        return reverse('news:details',kwargs={'pk':self.pk})