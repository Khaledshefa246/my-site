from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Comment, Reservation



class Dateinput(forms.DateInput):
    input_type = 'date'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }
        # help_texts = {
        #     "user_name": None,
        #     "user_email": None,
        #     "text": None,
        # }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ["branch"]
        # fields = "__all__"
        widgets = {'date' : Dateinput()}
        labels = {
            "user_name": "Your Name",
            "phone_number": "Phone Number",
            "date": "Date of Reservation",
            # "branch":"branch"
        }

class ReservationForm2(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ["branch"]
        # fields = "__all__"
        widgets = {'date' : Dateinput()}
        labels = {
            "user_name": "Name",
            "phone_number": "Number",
            "date": "Date of Reservation",
            # "branch":"branch"
        }