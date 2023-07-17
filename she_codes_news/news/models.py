from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(blank=True)
