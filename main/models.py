from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    page = models.IntegerField(
        default=0,
        verbose_name="Страница"
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главное"
        verbose_name_plural = "Главное"
    
    