from django import forms

class CommentForm(forms.Form):
    Comment = forms.CharField(label="Comment:", max_length=100)
