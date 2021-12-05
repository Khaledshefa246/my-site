#from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Post, Comment, Video, Reservation

from .forms import CommentForm, ReservationForm, ReservationForm2

from django.db.models import Value
from django.db.models.functions import Replace

from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.


def starting_page(request):
    #we use order bay
    latest_date = Post.objects.all().order_by("-date")[:3]
    latest_date_video = Video.objects.update(path_video = Replace('path_video', Value('watch?v='), Value('embed/')))
    latest_date_video = Video.objects.all().order_by("-date")[:3]
    # sorted_date = sorted(all_posts, key=get_date)
    # latest_date = sorted_date[-3:]

    return render(request, "blog/index.html", {
        "latest_date":latest_date,
        "latest_date_video":latest_date_video,
        # "path_video_replace":path_video_replace
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts":all_posts
    })

def Post_Category(request, pk):
    category = Category.objects.all()
    all_posts = Post.objects.filter(category_name = pk).order_by("-date")
    context = {
        "all_posts":all_posts,
        "category":category,
    }
    return render(request, "blog/all-posts.html", context)

def post_details(request, slug):
    # identified_post = next(post for post in all_posts if post["slug"]==slug)
    # we can do one of the next two lines the second one 
    # to 404 error page  
    # identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    post_tags = identified_post.tags.all()
    comment_form = CommentForm(request.POST)
    comments = identified_post.comments.all().order_by("-id")

    if comment_form.is_valid():
        # comment_form.use_required_attribute=False
        comment = comment_form.save(commit=False)
        comment.post = identified_post
        comment.save()
# we make redirection to reload the page but after clear the field of comment
        return HttpResponseRedirect(reverse("post_detail-page", args=[slug]))

    return render(request, "blog/post-detail.html", {
        "identified_post":identified_post,
        "post_tags":post_tags,
        "comment_form":comment_form,
        "comments":comments,
    })


def videos(request):
    all_videos = Video.objects.all().order_by("-date")
    context = {
        "all_videos":all_videos
    }
    return render(request, "blog/all-videos.html", context)


def about(request):
    return render(request, "blog/about.html")


def contactus(request):
    Reservations = ReservationForm(request.POST)
    Reservationmaadi = ReservationForm2(request.POST)
    if request.method == 'POST':
        Reservations = ReservationForm(request.POST, prefix='Heliopolis')
        if Reservations.is_valid():
            resr = Reservations.save(commit=False)
            resr.branch = "Heliopolis"
            resr.save()
    # we make redirection to reload the page but after clear the field of comment
            return HttpResponseRedirect(reverse("contact-us"))
    else:
        Reservations = ReservationForm(prefix='Heliopolis')

    if request.method == 'POST' and not Reservations.is_valid():
        Reservationmaadi = ReservationForm2(request.POST, prefix='Maadi')
        Reservations = ReservationForm(prefix='Heliopolis')
        if Reservationmaadi.is_valid():
            reser = Reservationmaadi.save(commit=False)
            reser.branch = "Maadi"
            reser.save()
    # we make redirection to reload the page but after clear the field of comment
            return HttpResponseRedirect(reverse("contact-us"))
    else:
        Reservationmaadi = ReservationForm2(prefix='Maadi')
        
    context = {"Reservations":Reservations, "Reservationmaadi":Reservationmaadi}
    return render(request, "blog/contactus.html", context)