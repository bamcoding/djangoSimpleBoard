from django.db import models

# Create your models here.
class User(models.Model):
  objects = models.Manager()
  memberid = models.CharField(max_length=50)
  email = models.EmailField()
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  createdts = models.DateTimeField(auto_now_add=True)
  modifiedts = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.memberid

  class Meta:
    db_table = 'users'