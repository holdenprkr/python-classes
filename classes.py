class Pizza:

    def __init__(self):
        self.size = 0
        self.style = ""
        self.toppings = list()

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        separator = ' and '
        print(
            f"I would like a {self.size}-inch, {self.style} pizza with {separator.join(self.toppings)}.")


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "thin crust"
meat_lovers.add_topping("bacon")
meat_lovers.add_topping("sausage")
meat_lovers.print_order()

pepperoni = Pizza()
pepperoni.size = 18
pepperoni.style = "deep dish"
pepperoni.add_topping("pepperoni")
pepperoni.print_order()