from django.db import models

class Bookmark(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    image = models.ImageField(blank=True,upload_to="images/", null=True)
    description = models.CharField(max_length=100) 
    star = models.IntegerField(default=0)

    def __str__(self):
        return self.name



