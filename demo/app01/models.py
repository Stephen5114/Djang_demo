from django.db import models
from account.models import User

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)