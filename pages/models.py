from django.db import models
from django.contrib.auth.models import User  
from django.utils import timezone
import uuid
STATUS = (
    (0,"Draft"),
    (1,"Publish"),
)
# Create your models here.
class Post(models.Model):
    """Model definition for Post."""
   
    # TODO: Define fields here
    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=250,default=uuid.uuid4,unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS,default=0)


    

    def __str__(self):
       return self.title + ' posted by |' + self.author.username
