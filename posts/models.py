from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')
class Article(models.Model):
    STATUS_OF_ARTICLES = (
        ("checking","Checking"),
        ("published","Published"),
        ("rejected","Rejected")
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    auther = models.ForeignKey(User , on_delete=models.CASCADE , related_name='Articles')
    status = models.CharField(max_length=12 , choices=STATUS_OF_ARTICLES , default="cheking")
    slug = models.SlugField(unique=True,null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d",blank=True,null=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            self.save()

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("blogs:blog_detail",kwargs={"slug":self.slug})


    def __str__(self):
        return f"{self.title} Writed by {self.auther}"

    objects = models.Manager()
    publish = PublishedManager()