from datetime import date
from random import randint


def calculate_age(birth_date):
    delta = date.today() - birth_date
    return (delta.days / 365).__floor__()


def generate_order_number():
    return randint(100000, 999999)
