from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получает данные по продуктам из кэша. Если кэш пуст, получает данные из БД и сохраняет в кэш."""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_products_by_category(category_id):
    """Возвращает список продуктов в указанной категории."""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id).select_related('category')

    key = f"products_category_{category_id}"
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.filter(category_id=category_id).select_related('category')
    cache.set(key, products, timeout=60*60)  # Кеш на 1 час
    return products