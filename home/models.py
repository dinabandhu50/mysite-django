from django.db import models

# Create your models here.
# makemigration meaning -  create changes and store in a file
# migrate  - apply the pending changes created by makemigrations
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    desc = models.TextField()
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name