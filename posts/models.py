from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # writer = models.ForeignKey(, on_delete=models.CASCADE)  # user foreignkey
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
