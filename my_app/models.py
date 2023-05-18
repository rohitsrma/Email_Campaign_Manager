from django.db import models
# Create your models here.
class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name}"
    
class UnsubscribedUser(models.Model):
    subscriber = models.OneToOneField(Subscribe, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return str(self.subscriber)
    

class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    text_content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.subject
    
