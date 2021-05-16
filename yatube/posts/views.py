from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Group
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


User = get_user_model()


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')

    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "group": group,
        "page": page
    }

    return render(request, "posts/group.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all().order_by("-pub_date")

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'author': author,
        "posts_count": author.posts.count()
    }

    return render(request, 'posts/profile.html', context)


def post_view(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, pk=post_id)

    context = {
        "post": post,
        "author": post.author,
        "posts_count": post.author.posts.count()
    }

    return render(request, "posts/post.html", context)


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
    form = PostForm()

    context = {
        "form": form,
    }

    return render(request, "posts/new_post.html", context)


@login_required
def post_edit(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, pk=post_id)

    if request.user == post.author:
        form = PostForm(instance=post, data=request.POST or None)

        if form.is_valid():
            form.save()

            return redirect('post', username=username, post_id=post_id)

        context = {
            'form': form,
        }

        return render(request, 'posts/post_edit.html', context)

    else:
        return redirect('post', username=username, post_id=post_id)
