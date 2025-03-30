def update_inventory(inventory: dict[str, int], product: str, quantity: int) -> None:
    if product in inventory:
        inventory[product] += quantity
        if inventory[product] <= 0:
            del inventory[product]
    elif quantity > 0:
        inventory[product] = quantity


def get_products_below_threshold(inventory: dict[str, int], quantity_threshold: int = 5) -> list:
    return [product for product, quantity in inventory.items() if quantity < quantity_threshold]


def print_heading(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def print_inventory(title: str, inventory: dict[str, int]) -> None:
    print_heading(title)
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'Product':<15} {'Quantity':>8}")
    print("-" * 25)
    for product, quantity in inventory.items():
        print(f"{product:<15} {quantity:>8}")
    print()


def print_low_stock_products(products: list[str]) -> None:
    print_heading("Products Below Threshold")
    if products:
        for product in products:
            print(f"- {product}")
    else:
        print("No products are below the threshold.")
    print()


def main() -> None:
    inventory = {
        "Apples": 10,
        "Bananas": 4,
        "Milk": 8,
        "Bread": 3,
        "Cheese": 4,
        "Fish": 2,
    }

    print_inventory("Inventory Before Changes", inventory)

    print("Updating inventory: Adding 5 to 'Apples':")
    update_inventory(inventory, "Apples", 5)
    print("=> Operation completed.\n")

    print("Updating inventory: Removing 2 from 'Bread':")
    update_inventory(inventory, "Bread", -2)
    print("=> Operation completed.\n")

    print("Updating inventory: Removing 3 from 'Fish' (this may delete the product if stock falls to 0 or below):")
    update_inventory(inventory, "Fish", -3)
    print("=> Operation completed.\n")

    print("Updating inventory: Adding 10 units of new product 'Carrots':")
    update_inventory(inventory, "Carrots", 10)
    print("=> Operation completed.\n")

    print_inventory("Inventory After Changes", inventory)

    low_stock_products = get_products_below_threshold(inventory)
    print_low_stock_products(low_stock_products)


if __name__ == "__main__":
    main()
