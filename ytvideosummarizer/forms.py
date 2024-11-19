from django import forms

class VideoURLForm(forms.Form):
    video_url = forms.URLField(label="Enter YouTube Video URL", widget=forms.URLInput(attrs={'class': 'form-control'}))
