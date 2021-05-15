from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['group', 'text']

        labels = {
            'group': ('Группа'),
            'text': ('Текст')
        }

        help_texts = {
            'group': ('Группа для этой записи'),
            'text': ('Текст этой записи')
        }
