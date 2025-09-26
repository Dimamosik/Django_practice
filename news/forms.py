from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
 feature/photo_upload
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
 main
        }
