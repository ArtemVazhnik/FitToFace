from django import forms
from blog.models import UserPhoto


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ('image', )
