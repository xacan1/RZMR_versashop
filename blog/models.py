from django.db import models
from django.urls import reverse
from shop.utils import slugify


def get_path_blog_image(instance, filename) -> str:
    return f'blog_photos/{instance.slug}/{filename}'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to=get_path_blog_image, max_length=255,
                              null=True, blank=True, verbose_name='Изображение')
    text = models.TextField(default='', blank=True, verbose_name='Текст поста')
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Создан')
    is_published = models.BooleanField(default=True, blank=True,
                                       verbose_name='Опубликован')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Пост: {self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
