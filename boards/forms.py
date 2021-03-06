from django import forms
from boards.models import Topic,Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget = forms.Textarea(attrs = {'rows':5,'placeholder':'Whats on your mind?'}),
    max_length = 400,
    help_text="The max length of this field is 4000",
    )
    class Meta:
        model = Topic
        fields = ['subject','message']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message',]
