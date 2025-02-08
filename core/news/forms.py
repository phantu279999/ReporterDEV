from django import forms
from django.utils.text import slugify

from core.news.models import Comment, News, NewsInZone, TagNews


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        # self.fields['slug'].widget.attrs['placeholder'] = 'Auto-generated from title'
        self.fields['title'].widget.attrs['oninput'] = "document.getElementById('id_slug').value = slugify(this.value)"

    def clean_slug(self):
        # Ensure the slug is auto-generated if empty
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data.get('title'))
        return slug


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]


from django.forms import inlineformset_factory

# Inline formsets for NewsInZone and TagNews
NewsInZoneFormSet = inlineformset_factory(
    News, NewsInZone, fields='__all__', extra=1
)

TagNewsFormSet = inlineformset_factory(
    News, TagNews, fields='__all__', extra=1
)