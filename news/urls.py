from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing_url'),
    path('news/', news_list, name='news_list_url'),
    path('news/<str:slug>/', news_detail, name='news_detail_url'),
    path('reviews/', reviews_list, name='reviews_list_url'),
    path('reviews/<str:slug>/', review_detail, name='review_detail_url'),

]
