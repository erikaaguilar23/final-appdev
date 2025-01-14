from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    # Other fields...

    def __str__(self):
        return self.title
