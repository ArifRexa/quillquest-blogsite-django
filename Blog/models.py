from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length= 100, unique = True)
    description = models.TextField(max_length = 255, blank = True)
    
    def __str__(self):
        return self.category_name

class BlogPost(models.Model):
    # Author of the blog post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=200, unique=True)

    # Title of the blog post
    title = models.CharField(max_length=200)

    # Content of the blog post (you can use TextField for longer content)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)

    # Date published (automatically set to the current date and time when created)
    published_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    # Optional fields for tags or categories (you can customize this)
    tags = models.CharField(max_length=100, blank=True, null=True)

    # Optional field for featured image (you can use ImageField)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']  # Sort posts by published date in descending order

