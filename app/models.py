from django.db import models

# Create your models here.
class info(models.Model):
    seq_no = models.IntegerField()
    title = models.CharField(max_length=200)
    timeline = models.CharField(max_length=200)
    text =  models.TextField(max_length=300)
    image = models.CharField(max_length=300)

    def __str__(self):
      return self.timeline