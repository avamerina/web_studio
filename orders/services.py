from orders.models import Order


def get_order_by_slug(slug):
    return Order.objects.get(slug=slug)


def process_order(slug):
    order = get_order_by_slug(slug)
    order.status = Order.PROCESSED
    order.save()
    return order
