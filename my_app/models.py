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
    
    def save(self, *args, **kwargs):
        self.subscriber.is_active = False  # Mark the associated Subscribe object as inactive
        self.subscriber.save()
        super().save(*args, **kwargs)


