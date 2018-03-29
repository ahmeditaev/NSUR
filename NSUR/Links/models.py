from django.db import models
from django.utils.timezone import now

# Create your models here.
class Facebook(models.Model):
   link = models.CharField(max_length=150,default='')
   published = models.DateTimeField(null=True, default=now())


class Twitter(models.Model):
   link = models.CharField(max_length=150,default='')
   published = models.DateTimeField(null=True, default=now())


class VK(models.Model):
   link = models.CharField(max_length=150,default='')
   published = models.DateTimeField(null=True, default=now())

   def publish(self):
      self.published = now()
      self.save()

   def __str__(self):
      return self.link

class Pinterest(models.Model):
   link = models.CharField(max_length=150,default='')
   published = models.DateTimeField(null=True, default=now())

   def publish(self):
      self.published = now()
      self.save()

   def __str__(self):
      return self.link


class Tumblr(models.Model):
   link = models.CharField(max_length=150,default='')
   published = models.DateTimeField(null=True, default=now())

   def publish(self):
      self.published = now()
      self.save()

   def __str__(self):
      return self.link

class Dribble(models.Model):
   link = models.CharField(max_length=150,default='')
   published = models.DateTimeField(null=True, default=now())

   def publish(self):
      self.published = now()
      self.save()

   def __str__(self):
      return self.link
