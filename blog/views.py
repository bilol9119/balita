from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Post, Tags, BioPost, Comment
from blog.Pagination import Pagination
from django.db.models import Count
from django.db.models import Q
# Create your views here.


def search_view(request):
    text = request.GET.get('blog')
    if text is not None:
        posts = (Post.objects.filter(title__contains=text))

    bio_post = BioPost.objects.order_by('-created_at')[0]

    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    tags = Tags.objects.all()[:10]
    context = {
        'posts': posts,
        'tags': tags,
        'popular_posts': popular_posts,
        'bio_post': bio_post,
        'latest_posts2': latest_posts2
    }
    return render(request, 'category.html', context=context)


def home_view(request):
    posts = Post.objects.order_by('-created_at')
    advertised_posts = Post.objects.order_by('-created_at').filter(is_advertised=True)[:3]
    tags = Tags.objects.all()[:10]
    bio_post = BioPost.objects.order_by('-created_at')[0]
    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]
    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    context = {
        'posts': posts,
        'paginator': paginator,
        'bio_post': bio_post,
        'tags': tags,
        'advertised_posts':advertised_posts,
        'popular_posts':popular_posts,
        'latest_posts2': latest_posts2

    }
    return render(request, 'index.html', context=context)


def about_view(request):
    latest_posts = Post.objects.order_by('-created_at')[0]
    posts = Post.objects.order_by('-created_at')[1:]
    bio_post = BioPost.objects.order_by('-created_at')[0]
    tags = Tags.objects.all()[:10]
    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    context = {
        'latest_posts': latest_posts,
        'posts': posts,
        'paginator': paginator,
        'bio_post': bio_post,
        'tags': tags,
        'popular_posts': popular_posts,
        'latest_posts2': latest_posts2
    }

    return render(request, 'about.html', context=context)


def category_view(request, name):
    page = request.GET.get('page', 1)

    posts = Post.objects.filter(category__name=name)
    paginator = Pagination(posts, 5)
    posts = paginator.get_page(page)

    bio_post = BioPost.objects.order_by('-created_at')[0]

    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    tags = Tags.objects.all()[:10]
    context = {
        'posts': posts,
        'tags': tags,
        'paginator': paginator,
        'popular_posts': popular_posts,
        'bio_post': bio_post,
        'latest_posts2':latest_posts2
    }
    return render(request, 'category.html', context=context)


def blog_single_view(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = Comment.objects.create(name=name, email=email, message=message, post_id=id)
        data.save()
        return redirect(f'/about/{id}/')

    post = Post.objects.filter(id=id).first()
    bio_post = BioPost.objects.order_by('-created_at')[0]
    tags = Tags.objects.all()[:10]
    comments = Comment.objects.filter(post_id=id).order_by('-created')
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)

    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    context = {
        'post': post,
        'bio_post': bio_post,
        'tags': tags,
        'comments': comments,
        'related_posts': related_posts,
        'popular_posts': popular_posts,
        'latest_posts2':latest_posts2
    }
    return render(request, 'blog-single.html', context=context)


def tag_view(request, id):
    posts = Post.objects.filter(tags=id)
    page = request.GET.get('page', 1)
    paginator = Pagination(posts, 5)
    posts = paginator.get_page(page)
    tags = Tags.objects.all()[:10]
    bio_post = BioPost.objects.order_by('-created_at')[0]

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]

    context = {
        'posts': posts,
        'tags': tags,
        'paginator': paginator,
        'bio_post': bio_post,
        'popular_posts':popular_posts,
        'latest_posts2': latest_posts2

    }
    return render(request, 'category.html', context=context)


def bio_view(request, id):
    posts = Post.objects.order_by('-created_at')[1:]
    bio_post = BioPost.objects.filter(id=id).first()
    tags = Tags.objects.all()[:10]

    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by(
        '-comment_count')[:3]

    context = {
        'latest_posts': bio_post,
        'posts': posts,
        'paginator': paginator,
        'bio_post': bio_post,
        'tags': tags,
        'popular_posts': popular_posts,
        'latest_posts2': latest_posts2
    }

    return render(request, 'about.html', context=context)


