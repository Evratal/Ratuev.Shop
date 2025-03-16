from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


# Список запрещенных слов
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]



class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = (" created_at","updated_at",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы Bootstrap ко всем полям
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')

        # Проверка на запрещенные слова в названии
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(
                    f"Запрещено использовать слово '{word}' в названии продукта"
                )

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        # Проверка на запрещенные слова в описании
        if description:
            for word in FORBIDDEN_WORDS:
                if word.lower() in description.lower():
                    raise ValidationError(
                        f"Запрещено использовать слово '{word}' в описании продукта"
                    )

        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Цена должна быть больше 0")
        return price
    # name = models.CharField(max_length=150, verbose_name='Наименование')
    # description = models.TextField(verbose_name="Описание", help_text= 'Введите описание продукта', blank=True, null=True)
    # image = models.ImageField(upload_to='catalog/image',  blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение товара')
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category',blank=True, null=True)
    # price = models.PositiveIntegerField( verbose_name='Цена')
    # created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')  # Установим текущее время на создание
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')  # Обновляем время при изменении