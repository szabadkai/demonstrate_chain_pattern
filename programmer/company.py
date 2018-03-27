class Company(object):

    def __init__(self, base_salary=2, employees=[]):
        self.employees = employees
        self.base_salary = base_salary

    def add_new_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return "\n".join([str(vars(emp)) for emp in self.employees])