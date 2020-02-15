from django.db import models
from django.contrib.auth.models import User  
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import uuid
STATUS = (
    (0,"Draft"),
    (1,"Publish"),
)
# Create your models here.
class Category (models.Model) : 
    category = models.CharField(max_length = 32,null = False )

    def __str__(self):
        return self.category
    
class Post(models.Model):
    """Model definition for Post."""
   
    # TODO: Define fields here
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ForeignKey(Category,default = 0,on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS,default=0)
    slug=models.SlugField(max_length=250,default=uuid.uuid4,unique=True)

    def __str__(self):
       return self.title + ' posted by |' + self.author.username

    def save(self,*args,**kwargs) : 
        
        self.slug = slugify(self.title,allow_unicode=True) 
        return super(Post,self).save(*args,**kwargs)

    def get_absolute_url(self,*args,**kwargs):
        # added direct link in the admin page to the related post 
        return reverse('post-detail', kwargs={'slug': self.slug})

