from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ["created_on"]

    def __str__(self):
        return (f"{self.title}")
