from django.db import models

class Blocktable(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    authId = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)
