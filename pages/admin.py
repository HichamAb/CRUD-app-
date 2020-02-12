from django.contrib import admin

# Register your models here.
from .models import Post 



class PostAdmin(admin.ModelAdmin) : 
    list_display = ["title","author","created_on","status","slug"]
    
    fieldsets = (
        ("Post Info", {
            'fields': (("title","author","slug"),"content")
                  
        }),
        ('Date && Status' , {
            'fields':("created_on","status")
        }),
    )
    

admin.site.register(Post,PostAdmin)
