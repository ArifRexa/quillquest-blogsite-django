from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.models import User
from Blog.models import BlogPost

# Create your views here.
def frontpage(request):
    blogs = BlogPost.objects.all()
    print(blogs)
    return render(request, 'core/frontpage.html', {'blogs':blogs})

def profile(request):
    # Retrieve the user by username
    # user = User.objects.get(username=username)
    
    # Retrieve all blog posts authored by the user
    blogs = BlogPost.objects.filter(author=request.user)

    return render(request, 'core/profile.html', {'blogs': blogs})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('frontpage')
    
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form':form})

def about(request):
    return render(request, 'core/about.html')
