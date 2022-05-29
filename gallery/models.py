from django.db import models

class Image(models.Model):
    location = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y", default='test')
    
    def __str__(self):
        return self.caption    

    
 

