from django.db import models
# Create your models here.

class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class UnsubscribedUser(models.Model):
    subscriber = models.ForeignKey(Subscribe, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subscriber)
    

class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    preview_text = models.TextField()
    article_url = models.URLField(blank=True)
    html_content = models.TextField(blank=True)
    text_content = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.subject
    
