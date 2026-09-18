"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # DONE: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        if qty < 1:
            raise ValueError("Need to select A quantity of 1 at least!")
        if not item['available']:
            raise OutOfStockError(f"Item {item['id']} not available in stock!")
        self.lines.append(item)

    def remove_item(self, item_id: int) -> None:
        for item in self.lines:
            if item['id'] == item_id:
                self.lines.remove(item)
                return
        #DONE: raise KeyError if the item is not in the cart
        raise KeyError(f"Item {item_id} cannot be removed, its not in the cart!")

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # DONE: demonstrate each rejection with try/except and a readable message.
    # Example:
    # try:
    #     cart.add_item(gyoza, 0)
    # except ValueError as e:
    #     print(f"Rejected: {e}")
    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f"Rejected: {e}")

    try:
        cart.add_item(miso, 2)
    except OutOfStockError as e:
        print(f"Rejected: {e}")

    try:
        cart.remove_item(-1)
    except KeyError as e:
        print(f"Rejected: {e}")
