from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=20,unique=True,null=False)
    description = models.TextField(max_length=200,null=True)

    image = models.ImageField(upload_to='project/',null=False)

    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.pk} : {self.title}'