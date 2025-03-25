from constants import INVENTORY


def update_inventory(inventory: dict, product: str, quantity: int) -> None:
    if product in inventory:
        inventory[product] += quantity
        if inventory[product] <= 0:
            del inventory[product]
    elif quantity > 0:
        inventory[product] = quantity


def stock_products(inventory: dict, count: int = 5) -> list:
    return [product for product, quantity in inventory.items() if quantity < count]


def main() -> None:
    print(f"Inventory before changes:\n{INVENTORY}")

    update_inventory(INVENTORY, "Apples", 5)
    update_inventory(INVENTORY, "Bread", -2)
    update_inventory(INVENTORY, "Fish", -3)
    update_inventory(INVENTORY, "Carrots", 10)

    print(f"\nInventory after changes:\n{INVENTORY}")

    print(f"\nProducts with quantity less than 5:\n{stock_products(INVENTORY)}")


if __name__ == "__main__":
    main()
