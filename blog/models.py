from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    """ モデルは__init__で属性を初期化しないほうがいいっぽい
    def __init__(self):
        super().__init__()
        # インスタンス変数は初期化メソッド内に書くべきという認識で合ってる？
        self.author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        self.title = models.CharField(max_length=200)
        self.text = models.TextField()
        self.created_date = models.DateTimeField(default=timezone.now)
        self.published_date = models.DateTimeField(blank=True, null=True)
    """

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
