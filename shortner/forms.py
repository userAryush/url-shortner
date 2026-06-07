from django import forms

from .models import ShortURL


class URLCreateForm(forms.ModelForm):
    custom_key = forms.CharField(required=False, max_length=10)
    expires_at = forms.DateTimeField(required=False)

    class Meta:
        model = ShortURL
        fields = ["original_url", "custom_key", "expires_at"]


class URLEditForm(URLCreateForm):
    pass

