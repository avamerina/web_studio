from core.celery import app
from orders.services import process_order as service_process


@app.task(ignore_results=False)
def process_order(order_slug):
    service_process(order_slug)
