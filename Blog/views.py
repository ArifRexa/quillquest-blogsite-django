from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def blogs(request):
    blogs = BlogPost.objects.filter(is_available = True) # all products
    # paginator = Paginator(products, 3) 
    # page = request.GET.get('page')
    # paged_product = paginator.get_page(page)
    # print(categories)
    # context = {'products' : paged_product}
    return render(request, 'blogs.html', {'blogs':blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def add_blog(request):
    return render(request, 'add_blog.html')


def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new blog post object but don't save it yet
            blog_post = form.save(commit=False)
            # Set the author to the currently logged-in user
            blog_post.author = request.user
            blog_post.save()
            return redirect('blogs')  # Redirect to the list of blogs or another page
    else:
        form = BlogPostForm()
    return render(request, 'add_blog.html', {'form': form})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'edit_blog.html'
    # fields = ['title', 'content', 'category', 'tags', 'featured_image', 'author_image']
    form_class = BlogPostForm
    success_url = reverse_lazy('profile')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blogs')