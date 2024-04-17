from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Contact
from blog.models import Tags, Post, BioPost
# Create your views here.


def contact_view(request):
    tags = Tags.objects.all()[:10]
    popular_posts = Post.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=0).order_by('-comment_count')[:3]
    bio_post = BioPost.objects.order_by('-created_at')[0]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        data = Contact.objects.create(name=name, email=email, message=message, phone=phone)
        data.save()
        return redirect('contact')

    latest_posts2 = Post.objects.order_by('-created_at')[:3]

    context = {
        'tags': tags,
        'posts': popular_posts,
        'bio_post': bio_post,
        'latest_posts2':latest_posts2
    }
    return render(request, 'contact.html', context=context)