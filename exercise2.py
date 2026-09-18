"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from exercise1 import load_menu # what are we importing here? Food for thought.

class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # DONE
        for new_item in self.lines:
            if new_item["name"] == item["name"]:
                new_item["qty"] += qty
                return

        item["qty"] = qty
        self.lines.append(item)

    def remove_item(self, item_id: int) -> None:
        # DONE
        for item in self.lines:
            if item["item_id"] == item_id:
                self.cart.remove(item)
                return

    def clear(self) -> None:
        # DONE
        self.lines.clear()

    def total(self) -> float:
        # DONE - round ONCE, at the end
        total_sum = sum([item["qty"] * item["price"] for item in self.lines])
        return round(total_sum, 2)

    def __repr__(self) -> str:
        # DONE

        current_cart = []
        for item in self.lines:
            current_cart.append(f"item_id: {item['id']} name: {item['name']}, qty: {item['qty']}")

        return str(current_cart)

if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)

    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
