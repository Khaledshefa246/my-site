from django.contrib import admin
from .models import Post, Author, Tag, Video, Category, Reservation

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    #the next line for make slug create automatic from title
    prepopulated_fields = {"slug":("title",)}

class VideoAdmin(admin.ModelAdmin):
    list_filter = ( "date",)
    list_display = ("title", "date", )
    #the next line for make slug create automatic from title
    prepopulated_fields = {"slug":("title",)}

class ReservationAdmin(admin.ModelAdmin):
    list_filter = ( "branch", "date")
    list_display = ("user_name", "phone_number", "date", "branch", )

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Video, VideoAdmin)
admin.site.register(Reservation, ReservationAdmin)
