from collections import defaultdict

SALES_DATA = [
    {"product": "Notebook", "quantity": 5, "price": 25000},
    {"product": "Phone", "quantity": 10, "price": 8000},
    {"product": "Headphones", "quantity": 20, "price": 1500},
    {"product": "Keyboard", "quantity": 15, "price": 800},
    {"product": "Mouse", "quantity": 30, "price": 400},
    {"product": "Monitor", "quantity": 8, "price": 6000},
    {"product": "Tablet", "quantity": 3, "price": 12000},
    {"product": "Charger", "quantity": 50, "price": 200},
    {"product": "USB Cable", "quantity": 100, "price": 100},
    {"product": "Screen Protector", "quantity": 70, "price": 150},
]


def calculate_revenue_by_product(sales_data: list[dict[str, str | int]]) -> dict[str, int]:
    revenue_by_product = defaultdict(int)

    for sale in sales_data:
        product = sale.get("product")
        quantity = sale.get("quantity", 0)
        price = sale.get("price", 0)
        revenue_by_product[product] += quantity * price

    return dict(revenue_by_product)


def get_high_revenue_products(revenue_dict: dict[str, int], revenue_threshold: int = 1000) -> list[str]:
    return [product for product, revenue in revenue_dict.items() if revenue > revenue_threshold]


def main() -> None:
    print(f"List with products:\n{SALES_DATA}")

    revenue_dict = calculate_revenue_by_product(SALES_DATA)
    print(f"\nDictionary of revenue by product:\n{revenue_dict}")

    high_revenue_products = get_high_revenue_products(revenue_dict)
    print(f"\nHigh revenue products:\n{high_revenue_products}")


if __name__ == "__main__":
   main()
