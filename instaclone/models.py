from django.db import models

# Create your models here.
class Image(models.Model):
    '''
    image Class for all images added to the app
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank = True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userId=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-post_date']

class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.IntegerField()

    def __str__(self):
        return self.comment