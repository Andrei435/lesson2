from django.db import models

class Blog (models.Model):

    blog_title = models.CharField(max_length=100)
    blog_date = models.DateTimeField()
    blog_text = models.CharField(max_length=500)
    blog_image = models.ImageField(upload_to='blog_images')

    def get_summary(self):
        return self.blog_text[:70]

    def __str__(self):
        return self.blog_title