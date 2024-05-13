class shoppingCart:
    def __init__(self):
        self.items = []


    def add_item(self, item_name, quantity, price):

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
        total_cost =sum(item_prices.get(item, 0) * quantity for item, quantity in self.items.items())
        return total_cost
    