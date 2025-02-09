from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name="Описание", help_text= 'Введите описание продукта', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name="Описание", help_text= 'Введите описание продукта', blank=True, null=True)
    image = models.ImageField(upload_to='catalog/image',  blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение товара')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category',blank=True, null=True)
    price = models.PositiveIntegerField( verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')  # Установим текущее время на создание
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')  # Обновляем время при изменении

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']



