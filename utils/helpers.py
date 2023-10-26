from datetime import date


def calculate_age(birth_date):
    delta = date.today() - birth_date
    return (delta.days / 365).__floor__()
