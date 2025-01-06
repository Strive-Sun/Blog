from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('分类名', max_length=100)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Post(models.Model):
    title = models.CharField('标题', max_length=200)
    content = RichTextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    views = models.PositiveIntegerField('阅读量', default=0)
    featured_image = models.ImageField('特色图片', upload_to='blog/%Y/%m/', blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

class Theme(models.Model):
    name = models.CharField('主题名称', max_length=100)
    primary_color = models.CharField('主色调', max_length=7, default='#007bff')
    secondary_color = models.CharField('次要色调', max_length=7, default='#6c757d')
    background_color = models.CharField('背景色', max_length=7, default='#ffffff')
    text_color = models.CharField('文字颜色', max_length=7, default='#212529')
    is_active = models.BooleanField('是否启用', default=False)

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_active:
            Theme.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)
