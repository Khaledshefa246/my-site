from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "posts", null = True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
    category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="categorys")
    pdf_word_file = models.FileField(upload_to="pdf word", null=True, max_length=150)


class Comment(models.Model):
    user_name = models.CharField(max_length=120, help_text=None)
    user_email = models.EmailField(help_text=None)
    text = models.TextField(max_length=400, help_text=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


class Video(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    path_video = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)


class Reservation(models.Model):
    branch_choices = [
        ("Heliopolis", "Heliopolis"),
        ("Maadi", "Maadi")
    ]

    user_name = models.CharField(max_length=120, help_text=None)
    phone_number= models.CharField(max_length=14, null=True, blank=True, help_text=None)
    date = models.DateField(help_text=None)
    branch = models.CharField(max_length=120, choices = branch_choices)


