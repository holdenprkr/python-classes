class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date


class Company:
    def __init__(self, business_name, address, industry):
        self.business_name = business_name
        self.address = address
        self.industry = industry
        self.employees = list()


bob = Employee("Bob", "Developer", "08/30/2019")
jan = Employee("Jan", "Manager", "9/12/2019")
susan = Employee("Susan", "Manager", "9/1/2019")
jack = Employee("Jack", "Director of Sales", "10/5/2019")
john = Employee("John", "Developer", "10/25/2019")

big_company = Company("Big Company", "300 Big St", "Sales")
small_company = Company("Small Company", "10 Small Way", "Furniture Store")

big_company.employees.append(bob)
big_company.employees.append(jack)
big_company.employees.append(susan)

small_company.employees.append(jan)
small_company.employees.append(john)

print(f"{big_company.business_name} is in the {big_company.industry} industry and has the following employees")
for employee in big_company.employees:
    print(f"    * {employee.name}")

print(f"{small_company.business_name} is in the {small_company.industry} industry and has the following employees")
for employee in small_company.employees:
    print(f"    * {employee.name}")
