from django import forms

POST_STATUS_CHOICES = (('PUB','Published'),('UP','Unpublished'),('B','Blocked'))

class PostForm(forms.Form):
    title = forms.CharField(label='Post Title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(choices = POST_STATUS_CHOICES, label="Post Status", initial='UP', widget=forms.Select(), required=True)