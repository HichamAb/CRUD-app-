from django.contrib import admin

# Register your models here.
from .models import Post , Category



class PostAdmin(admin.ModelAdmin) : 
    list_display = ["title","categories","author","created_on","status","slug"]
    
    fieldsets = (
        ("Post Info", {
            'fields': ("title","categories","author","slug","content")
                  
        }),
        ('Date && Status' , {
            'fields':("created_on","status")
        }),
    )
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
