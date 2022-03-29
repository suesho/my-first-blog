from django import forms

from .models import Post


# PostForm=フォームの名前
class PostForm(forms.ModelForm):

    # Djangoに、フォームを作る際どのモデルを使うか教えるためのクラス
    class Meta:
        model = Post
        fields = ('title', 'text',)
