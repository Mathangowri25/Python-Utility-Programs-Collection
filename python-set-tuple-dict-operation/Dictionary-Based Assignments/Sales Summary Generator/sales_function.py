def get_top_city(sales: dict) -> str:
    if not sales:
        return "" 
    return max(sales, key=sales.get)


def get_low_sales_cities(sales: dict, threshold: int) -> dict:
    return {city: amount for city, amount in sales.items() if amount < threshold}


def increase_sales(sales: dict, percentage: float) -> dict:
    return {city: int(amount * (1 + percentage / 100)) for city, amount in sales.items()}
