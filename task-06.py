# 6.Inventory Management with Constraints
# Manage product inventory:
# add/remove items
# track quantity
# block selling more than available
# warn when stock < threshold


import warnings


class Item:
    def __init__(self, name, quantity) -> None:
        # Verification
        if quantity < 0:
            raise ValueError("Quantity Can't be negative.")
        self.name = name
        self.quantity = quantity
        self.threshold = quantity * 0.2

    def __str__(self) -> str:
        return f"Item: {self.name} has: {self.quantity} quantity"


class Inventory:
    def __init__(self) -> None:
        self.items = {}

    def add_items(self, name, item_id, quantity):
        if item_id in self.items.keys():
            self.items[item_id].quantity += quantity
        else:
            self.items[item_id] = Item(name, quantity)

    def remove_items(self, item_id, quantity_to_delete):
        if self.items[item_id].quantity < quantity_to_delete:
            raise ValueError(
                f"Items quantity Not sufficient to delete, it's {self.items[item_id].quantity}"
            )
        else:
            self.items[item_id].quantity -= quantity_to_delete
            if self.items[item_id].quantity <= self.items[item_id].threshold:
                warnings.warn(
                    f"The Item stock acceded the threshold {self.items[item_id].threshold}"
                )

    def display_items(self):
        for item in self.items.values():
            print(item)

    def sell_items(self, item_id, quantity_to_sale):
        if self.items[item_id].quantity < quantity_to_sale:
            raise ValueError(
                f"Items inventory Not sufficient to Sale, it's {self.items[item_id].quantity}"
            )
        else:
            self.items[item_id].quantity -= quantity_to_sale
            if self.items[item_id].quantity <= self.items[item_id].threshold:
                warnings.warn(
                    f"The Item stock acceded the threshold {self.items[item_id].threshold}"
                )


inventory = Inventory()
inventory.add_items("laptop", 1, 1000)
inventory.add_items("phone", 2, 2000)
inventory.display_items()
print("----------------------------------")
print(inventory.remove_items(1, 900))
# print(inventory.sell_items("laptop", 1, 100))
inventory.display_items()
