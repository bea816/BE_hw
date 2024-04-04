from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def increase_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title

#모델 migrate 안 하면 에러난다. 잊지말자