from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(verbose_name='Дата создания')
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name} {self.category} {self.purchase_price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
