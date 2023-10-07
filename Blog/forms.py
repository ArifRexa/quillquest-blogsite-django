# forms.py
from django import forms
from .models import BlogPost
from django.views.generic.edit import UpdateView



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'tags', 'featured_image', 'author_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': ' mb-12  block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': 'Enter title', 'label':"Blogs Title"}),
            
            
            'content': forms.Textarea(attrs={'class': 'mb-12 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'rows': 5, 'placeholder': 'Enter content'}),
            # 'content': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'rows': 5, 'placeholder': 'Enter content'}),
            
            
            'category': forms.Select(attrs={'class': 'mb-12 bg-white border border-white text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Choose Category'}),
            
            
            'tags': forms.TextInput(attrs={'class': 'mb-12 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': 'Enter tags'}),
            
            
            'featured_image': forms.ClearableFileInput(attrs={'class': 'mb-12 block w-full text-sm text-black border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-black focus:outline-none dark:bg-white dark:border-gray-600 dark:placeholder-gray-400'}),

            'author_image': forms.ClearableFileInput(attrs={'class': 'mb-12 block w-full text-sm text-black border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-black focus:outline-none dark:bg-white dark:border-gray-600 dark:placeholder-gray-400'}),
        }
