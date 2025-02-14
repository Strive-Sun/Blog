# Generated by Django 4.2.3 on 2025-01-06 15:40

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='主题名称')),
                ('primary_color', models.CharField(default='#007bff', max_length=7, verbose_name='主色调')),
                ('secondary_color', models.CharField(default='#6c757d', max_length=7, verbose_name='次要色调')),
                ('background_color', models.CharField(default='#ffffff', max_length=7, verbose_name='背景色')),
                ('text_color', models.CharField(default='#212529', max_length=7, verbose_name='文字颜色')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('featured_image', models.ImageField(blank=True, upload_to='blog/%Y/%m/', verbose_name='特色图片')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-created_time'],
            },
        ),
    ]
