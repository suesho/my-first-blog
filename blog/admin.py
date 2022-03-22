from django.contrib import admin
from .models import Post

# Adminページ(管理画面)上で見えるようにするため、モデルを登録
admin.site.register(Post)
