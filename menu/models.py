from django.db import models
from django.utils import timezone
from datetime import timedelta


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    calories = models.PositiveIntegerField(verbose_name="Калории")
    proteins = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Белки")
    fats = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Жиры")
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Углеводы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class DishProduct(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    grams = models.PositiveIntegerField(verbose_name="Кол-во")  # Количество грамм продукта в блюде

    def __str__(self):
        return f"{self.dish.name} - {self.product.name} ({self.grams} г)"

    class Meta:
        verbose_name = "Создание рецепта"
        verbose_name_plural = "Создание рецептов"


class SaveMenuDishAndProductsManager(models.Manager):
    def get_recently_created_items(self):
        one_minute_ago = timezone.now() - timedelta(minutes=0.1)
        return self.filter(creation_date__gte=one_minute_ago)


class SaveMenuDishAndProducts(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    grams = models.PositiveIntegerField(verbose_name="Кол-во")  # Количество грамм продукта в блюде
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True, blank=True)

    objects = SaveMenuDishAndProductsManager()  # Привязываем менеджер к модели

    def __str__(self):
        return f"{self.dish.name} - {self.product.name} ({self.grams} г)"

    class Meta:
        verbose_name = "Сохранение рецепта"
        verbose_name_plural = "Сохранение рецептов"
