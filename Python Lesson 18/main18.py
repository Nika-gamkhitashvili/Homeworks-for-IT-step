class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"


class House:
    def __init__(self, ID, price, owner, status="for sale"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell(self, buyer, loan_amount=None):

        if loan_amount:
            # Adjust buyer's deposit and loan
            buyer.deposit -= loan_amount
            buyer.loan += loan_amount

            # Update house owner and status
            self.owner = buyer
            self.status = "Sold on loan"
            print(f"House {self.ID} sold to {buyer.name} on loan.")
        else:
            # Update house owner and status
            self.owner = buyer
            self.status = "Sold"
            print(f"House {self.ID} sold to {buyer.name}.")


owner = Person("nika", 2000)
buyer = Person("giorgi", 1500)

house = House("0222100150", "40000$", owner)

house.sell(buyer)

print(house.ID, house.price)
print(owner)
