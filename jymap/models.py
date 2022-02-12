from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    start_time = models.DateTimeField("시작시간")
    end_time = models.DateTimeField("마감시간")
    title = models.CharField("이벤트 이름", max_length=50)
    description = models.TextField("상세")
    image = models.ImageField(upload_to='images/',blank=True)
    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class ImageFile(models.Model):
    post = models.ForeignKey(Event, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images/',blank=True, null = True)