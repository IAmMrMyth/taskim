from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=128)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField("Completed", default=False)
    archive = models.BooleanField("archive", default=False)

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        return "/"
    
    def __str__(self):
        return self.title

