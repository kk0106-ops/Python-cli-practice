class Merchandise:
    def __init__(self, id, name, price, purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

    def cost_accounting(self):
        cost_rate = self.purchase_price / self.price
        return cost_rate

Product_overview = Merchandise("A0001", "半袖クールTシャツ", 5000, 2250)
cost_rate = Product_overview.cost_accounting()
print(cost_rate)

cost_rate = Product_overview.cost_accounting()
print(cost_rate)

