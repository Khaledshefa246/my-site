from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page, name='starting-page'),
    path("posts/",views.posts, name='post-page'),
    path("postcategory/<str:pk>",views.Post_Category, name='post-page-category'),
    path("videos/",views.videos, name='video-page'),
    path("about/",views.about, name='about'),
    path("contactus/",views.contactus, name='contact-us'),
    path("posts/<slug:slug>",views.post_details, name="post_detail-page") #/posts/my-fisrt-post
]
