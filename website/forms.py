from django import forms
from django.forms import ModelForm
from .models import UserData, Comments

class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ('name', 'surname', 'phone', 'birth', 'email')


class CreateComment(ModelForm):
    class Meta:
        model = Comments
        fields = ('title', 'body')


