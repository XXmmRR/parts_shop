from django.db import models

# Create your models here.


class Mark(models.Model):
    mark_name = models.CharField(max_length=250,  verbose_name='Название марки')
    mark_slug = models.SlugField(max_length=255, verbose_name='Слаг поле марки')
    image = models.ImageField(upload_to='images/shop', blank=True)

    class Meta:
        db_table = "Марка"
        verbose_name_plural = "Марки"

    def __str__(self):
        return self.mark_name


class Model(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='mark')
    model_name = models.CharField(max_length=255, verbose_name='Название модели')
    model_slug = models.SlugField(max_length=255, verbose_name='Слаг поле модели')
    image = models.ImageField(upload_to='images/shop')

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = "Модель"
        verbose_name_plural = "Модели"


class Category(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True, null=True,  related_name='model')
    category_name = models.CharField(max_length=250, verbose_name='Название категории',)
    category_slug = models.SlugField(max_length=250, verbose_name='Слаг поле категории',)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "Категория"
        verbose_name_plural = "Категории"


class Part(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='category')
    article = models.CharField(max_length=255, verbose_name='Оригинальный артикул')
    article_second = models.CharField(max_length=255, verbose_name='Дополнительный артикул')
    part_name = models.CharField(max_length=255, verbose_name='Наименование')
    part_exist = models.BooleanField(verbose_name='Наличие')
    part_slug = models.SlugField(max_length=250, verbose_name='Слаг')
    part_price = models.IntegerField(verbose_name='Цена запчасти')
    image = models.ImageField(upload_to='images/shop',)

    def __str__(self):
        return f'{self.part_name}:{self.part_price}'

    class Meta:
        db_table = "Деталь"
        verbose_name_plural = 'Детали'