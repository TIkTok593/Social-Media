from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image

import requests


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):  # This method will triggered when form.is_valid() method called
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given url doesn\'t exist' \
                                        'match valid image extension.')
        return url

    def save(self, commit=True, force_insert=False, force_update=False):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit(".", 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = requests.get(image_url)  # Download the image from the provided url
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)  # here we didn't save it because this is only the image attribute in the model
                                      # We want to save the image object itself
        if commit:
            image.save()
        return image
