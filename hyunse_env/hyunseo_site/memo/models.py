from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from .utils import Utils

# Create your models here.
class Memo(models.Model):
    content = models.TextField(max_length=250, null=True, blank=False)
    content_color = models.CharField(max_length=20, choices=Utils.get_content_color_choicelist(), default='teal')
    created_at = models.DateTimeField(auto_now_add=True)
    
    #class Meta:
    def delete(self, *args, **kwargs):
        super(Memo, self).delete(*args, **kwargs)
        
        