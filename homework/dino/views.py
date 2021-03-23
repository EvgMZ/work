from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.contrib.auth.models import User
from django.core.paginator import Paginator
def post(request, username, post_id):
    post = get_object_or_404(Post, pk=post_id, author__username=username)
    author = post.author
    return render(request, 'post.html', {
                                        'author': author,
                                        'post': post})

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator}
       )

def posts_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.grposts.all()[:12]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "group.html", {"group": group,
                                          "posts": posts,
                                          "paginator": paginator,
                                          "page": page})