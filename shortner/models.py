from django.db import models
from Base.models import BaseModel
from django.conf import settings


class ShortURL(BaseModel):
    original_url = models.URLField()

    # Short key (e.g. abc123)
    short_key = models.CharField(max_length=10,unique=True)

    click_count = models.IntegerField(default=0)
    expires_at = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='short_urls')

    def __str__(self):        
        return self.short_key