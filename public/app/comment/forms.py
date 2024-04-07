# Django
from django import forms
# Application
from .models import Comment


class CommentForm(forms.ModelForm):
    type_source = forms.CharField(widget=forms.HiddenInput(), required=False)
    type_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    content = forms.CharField(widget=forms.Textarea, required=True, label="Текст комментария")

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit=commit)

    class Meta:
        model = Comment
        fields = ('type_source', 'type_id', 'content')
