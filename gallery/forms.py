from django import forms
from .models import Image

# What we want to display in the forms
class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            "location",
            "category",
            "caption",
            "image",
        )
        
class ImageForms(forms.Form):
    location = forms.CharField()
    category = forms.CharField()
    caption = forms.CharField()
    header_image = forms.ImageField()
    
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","image")    
