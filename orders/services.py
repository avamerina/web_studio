from orders.models import Order


def get_order_by_slug(slug):
    return Order.objects.get(slug=slug)
