from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from blog.models import Blog


# Create your views here.
@cache_page(60 * 15)
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog/blog_detail.html", {"blog": blog})
