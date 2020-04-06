from django.db import models

# Create your models here.
class Board(models.Model):
  objects = models.Manager()
  title = models.CharField(verbose_name='제목', max_length=100)
  content = models.TextField(verbose_name='내용')
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)
  createdts = models.DateTimeField(auto_now_add=True)
  modifiedts = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'boards'