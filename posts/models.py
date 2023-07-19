from django.db import models
from django.contrib.auth import get_user_model

from django.conf import settings


User = get_user_model()

class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # user foreignkey
    category_choices = (('일반', '일반'), ('공지사항', '공지사항'))
    category = models.CharField(max_length=20, choices=category_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 조회수
    hit = models.PositiveIntegerField(default=0)
    # 이미지
    img = models.ImageField(upload_to="", blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
