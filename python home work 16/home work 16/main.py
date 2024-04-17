class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):

        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name):

        if item_name in self.items:
            del self.items[item_name]

    def current_items(self):

        return self.items

    def calculate_total(self):

        item_prices = {
            "პური": 2.5,
            "ზეთი": 5.0,
            "კარაქი": 1.0,
            "წყალი": 1.2
        }
        total_cost = sum(item_prices.get(item, 0) * quantity for item, quantity in self.items.items())
        return total_cost


cart = ShoppingCart()
cart.add_item("პური", 2)
cart.add_item("ზეთი", 1)
cart.add_item("კარაქი", 6)
cart.add_item("წყალი", 3)

print("Current items in the shopping cart:")
for item, quantity in cart.current_items().items():
    print(f"{item}: {quantity}")

print(f"Total cost: {cart.calculate_total():.2f}ლ")
cart.remove_item("პური")
print("Total cost after remove:", f"{cart.calculate_total()}ლ")

#
# meore varianti
# class Kalata:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
#
#
# kalata = Kalata("პურო", 1.2)
# kalata2 = Kalata("კარაქი", 5.5)
# kalata3 = Kalata("წყალი", 0.6)
# kalata4 = Kalata("ზეთი", 7.8)
# print(kalata.name, kalata.value)
# print(kalata2.name, kalata2.value)
# print(kalata3.name, kalata3.value)
# print(kalata4.name, kalata4.value)
# full_value = kalata.value + kalata2.value + kalata3.value + kalata4.value
# print('ჯამური ღირებულება:', full_value)
