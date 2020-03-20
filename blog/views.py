from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def allBlogs(request):
    blogs = Blog.objects
    return render(request, 'blog/bloghome.html',{'blogs':blogs})

def detail(request, blog_id):
    blogdetail  = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/blogdetail.html', {'blogdetail': blogdetail})
    