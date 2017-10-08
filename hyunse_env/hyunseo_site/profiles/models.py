from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from .utils import Utils
# Create your models here.
class Task(models.Model):
    content = models.TextField(max_length=250, null=True, blank=False)
    duedate = models.DateField()
    tag = models.CharField(max_length=100, choices=Utils.get_tag_choicelist(), default='TODO',)
    tag_color = models.CharField(max_length=20, choices=Utils.get_tag_color_choicelist(), default='teal',)
    checked = models.BooleanField(default=False)
    checked_at = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        super(Task, self).delete(*args, **kwargs)
