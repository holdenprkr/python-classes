from building import Building
from city import City

megalopolis = City("Megalopolis", "Jimmy", 2020)

one = Building("11 1st Street", 11)
two = Building("22 2nd Street", 12)
three = Building("33 3rd Street", 13)
four = Building("44 4th Street", 14)
five = Building("55 5th Street", 17)

one.purchase("Daniel")
two.purchase("Morgan")
three.purchase("Lisa")
four.purchase("Lauren")
five.purchase("Donald")

one.construct()
two.construct()
three.construct()
four.construct()
five.construct()

megalopolis.add_building(one)
megalopolis.add_building(two)
megalopolis.add_building(three)
megalopolis.add_building(four)
megalopolis.add_building(five)

for building in megalopolis.buildings:
    print(f"{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.")
