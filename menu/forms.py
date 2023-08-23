from django import forms
from .models import *


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name']


class DishProductForm(forms.ModelForm):
    class Meta:
        model = DishProduct
        fields = ['product', 'grams']


DishProductFormSet = forms.inlineformset_factory(
    Dish, DishProduct, form=DishProductForm, extra=6, max_num=6, can_delete=True
)


class DeleteDishForm(forms.Form):
    dish = forms.ModelChoiceField(queryset=Dish.objects.all(), label="Выберите блюдо")


class DeleteProductForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label="Выберите продукт для удаления"
    )


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Наименование')
    calories = forms.IntegerField(label='Калории')
    proteins = forms.DecimalField(label='Белки')  # Используйте DecimalField для десятичных значений
    fats = forms.DecimalField(label='Жиры')  # Используйте DecimalField для десятичных значений
    carbohydrates = forms.DecimalField(label='Углеводы')  # Используйте DecimalField для десятичных значений


DishProductFormSet = forms.inlineformset_factory(
    Dish, DishProduct, form=DishProductForm, extra=8, max_num=8, can_delete=True
)


class DishProductForm(forms.ModelForm):
    class Meta:
        model = DishProduct
        fields = ['dish', 'product', 'grams']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()


class BreakfastForm(forms.Form):
    dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple)
