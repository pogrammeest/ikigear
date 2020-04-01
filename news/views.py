from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import *

from .API import *


def landing(request):
    posts = Post.objects.all()
    reviews = Review.objects.all()
    previews = Slider.objects.all()
    return render(request, 'news/landing.html', context={'posts': posts, 'reviews': reviews, 'previews': previews})


def news_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    return render(request, 'news/news_list.html', context={'posts': posts})


def news_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, 'news/news_detail.html', context={'post': post})


def reviews_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        reviews = Review.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        reviews = Review.objects.all()
    return render(request, 'reviews/reviews_list.html', context={'reviews': reviews})


def review_detail(request, slug):
    review = get_object_or_404(Review, slug__iexact=slug)
    return render(request, 'reviews/review_detail.html', context={'review': review})


def not_working(request):
    return render(request, 'working/not_working.html')


def ikiwinner(request):
    return render(request, 'working/ikiwinner.html')


def call_view(request):
    data = request.GET
    update_slider()
    print(data)
    print("\n", HttpResponse.status_code, "- Вышло новое видео, изменяем слайдер!\n")
    return HttpResponse('')
