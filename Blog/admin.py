from django.contrib import admin
from .models import Category, BlogPost

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name', 'slug')



     
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost)
# admin.site.register(BlogPost)
