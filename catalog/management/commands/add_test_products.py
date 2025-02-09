from django.core.management.base import BaseCommand
from catalog.models import Product  # Замените your_app на название вашего приложения

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Удаление всех существующих продуктов...'))
        Product.objects.all().delete()  # Удаляем все существующие продукты

        # Список тестовых продуктов
        test_products = [
            {
                'name': 'Тестовый продукт 1',
                'price': 100,
            },
            {
                'name': 'Тестовый продукт 2',
                'price': 200,
            },
            {
                'name': 'Тестовый продукт 3',
                'price': 300,
            },
        ]

        # Добавление тестовых продуктов в базу данных
        for product_data in test_products:
            product = Product(
                name=product_data['name'],
                price=product_data['price'],
            )
            product.save()

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены.'))