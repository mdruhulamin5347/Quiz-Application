from django.db import models



class ContactModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)  # Use CharField for length limitation

    def __str__(self):
        return self.name or ""
