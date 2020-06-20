from django.db import models
from django.utils import timezone


class blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_name = models.CharField(max_length=180, null=True)
    blog_body = models.TextField(null=True)
    blog_technology = models.CharField(max_length=180, null=True)
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=1)  # 0:Inactive 1:Active
    created_by = models.PositiveIntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_by = models.PositiveIntegerField(null=True, blank=True)
    updated_on = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
