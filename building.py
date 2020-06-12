import datetime


class Building:
    def __init__(self, address, stories):
        self.designer = "Holden Parker"
        self.date_constructed = datetime
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner


one_hundred_first = Building("100 1st Street", 11)
two_hundred_second = Building("200 2nd Street", 12)
three_hundred_third = Building("300 3rd Street", 13)
four_hundred_fourth = Building("400 4th Street", 14)
five_hundred_fifth = Building("500 5th Street", 15)

one_hundred_first.purchase("Bob")
two_hundred_second.purchase("Bill")
three_hundred_third.purchase("Nancy")
four_hundred_fourth.purchase("Debbie")
five_hundred_fifth.purchase("William")

one_hundred_first.construct()
two_hundred_second.construct()
three_hundred_third.construct()
four_hundred_fourth.construct()
five_hundred_fifth.construct()

print(f"{one_hundred_first.address} was purchased by {one_hundred_first.owner} on {one_hundred_first.date_constructed} and has {one_hundred_first.stories} stories.")
print(f"{two_hundred_second.address} was purchased by {two_hundred_second.owner} on {two_hundred_second.date_constructed} and has {two_hundred_second.stories} stories.")
print(f"{three_hundred_third.address} was purchased by {three_hundred_third.owner} on {three_hundred_third.date_constructed} and has {three_hundred_third.stories} stories.")
print(f"{four_hundred_fourth.address} was purchased by {four_hundred_fourth.owner} on {four_hundred_fourth.date_constructed} and has {four_hundred_fourth.stories} stories.")
print(f"{five_hundred_fifth.address} was purchased by {five_hundred_fifth.owner} on {five_hundred_fifth.date_constructed} and has {five_hundred_fifth.stories} stories.")
