from collections import defaultdict


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


def print_heading(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def print_sales_data(sales_data: list[dict[str, str | int]]) -> None:
    print_heading("Sales Data")
    print(f"{'Product':<20} {'Quantity':>8} {'Price':>10}")
    print("-" * 40)
    for sale in sales_data:
        product = sale.get("product", "Unknown")
        quantity = sale.get("quantity", 0)
        price = sale.get("price", 0)
        print(f"{product:<20} {quantity:>8} {price:>10}")
    print()


def print_revenue_by_product(revenue_dict: dict[str, int]) -> None:
    print_heading("Revenue by Product")
    print(f"{'Product':<20} {'Revenue':>10}")
    print("-" * 32)
    for product, revenue in revenue_dict.items():
        print(f"{product:<20} {revenue:>10}")
    print()


def print_high_revenue_products(products: list[str]) -> None:
    print_heading("High Revenue Products")
    if products:
        for product in products:
            print(f"- {product}")
    else:
        print("No products exceed the revenue threshold.")
    print()


def main() -> None:
    sales_data = [
        {"product": "Notebook", "quantity": 5, "price": 25000},
        {"product": "Phone", "quantity": 10, "price": 8000},
        {"product": "Headphones", "quantity": 20, "price": 1500},
        {"product": "Keyboard", "quantity": 15, "price": 800},
        {"product": "Mouse", "quantity": 2, "price": 400},
        {"product": "Monitor", "quantity": 8, "price": 6000},
        {"product": "Tablet", "quantity": 0, "price": 1000},
        {"product": "Charger", "quantity": 6, "price": 200},
        {"product": "USB Cable", "quantity": 9, "price": 100},
        {"product": "Screen Protector", "quantity": 3, "price": 150},
    ]

    print_sales_data(sales_data)

    revenue_dict = calculate_revenue_by_product(sales_data)
    print_revenue_by_product(revenue_dict)

    high_revenue_products = get_high_revenue_products(revenue_dict)
    print_high_revenue_products(high_revenue_products)


if __name__ == "__main__":
    main()
