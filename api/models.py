from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    written_by = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title