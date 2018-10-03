import markdown

from django.db import models
from django.shortcuts import reverse
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(verbose_name='名称', max_length=16)

    class Meta:
        db_table = 't_tag_info'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=16)
    author = models.ForeignKey(User, verbose_name='作者')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    content = models.TextField(verbose_name='内容', null=True, blank=True)
    count = models.IntegerField(verbose_name='点击量', default=0)
    excerpt = models.CharField(verbose_name='文章摘要', max_length=72, null=True, blank=True)
    mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    
    class Meta:
        db_table = 't_blog_info'
        ordering = ['-ctime', ]
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.id),])

    def increase_views(self):
        self.count += 1
        self.save(update_fields=['count'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:66]
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + '------>' + self.author.username


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='所属文章')
    username = models.CharField(verbose_name='用户名', max_length=16)
    email = models.EmailField(verbose_name='邮箱')
    content = models.TextField(verbose_name='评论')
    ip = models.GenericIPAddressField(verbose_name='用户ip', editable=False, default='')
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 't_comment_info'
        verbose_name = '评论'
        verbose_name_plural = verbose_name
