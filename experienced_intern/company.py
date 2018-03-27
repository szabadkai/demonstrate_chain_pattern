from employee import Employee
from emp_types import CEO, Senior, Junior


class Company(object):

    employees = []
    base_salary = 2

    def ceo(self):
        associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'senior partner', self.employees))
        salary = self.base_salary * 5 * max([len(self.employees), 1])

        return associates, salary

    def senior(self):
        salary = self.base_salary * 5 * max([len(self.employees), 1]) * 0.80
        associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'junior partner', self.employees))

        return associates, salary

    def junior(self):
        salary = self.base_salary * 3
        associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'minion', self.employees))

        return associates, salary

    def add_new_employee(self, data):
        """
        :param data:
        :return:
        """

        title = data['title']
        associates = []

        if title == 'CEO':
            employee = CEO(**data)
            associates, salary = self.ceo()

        elif title == 'Senior partner':
            employee = Senior(**data)
            associates, salary = self.senior()
            employee.car = 'VW Passat' if salary > 20 else 'VW Jetta'

        elif title == 'Junior partner':
            employee = Junior(**data)
            associates, salary = self.junior()

        else:
            employee = Employee(**data)
            salary = self.base_salary

        employee.salary = salary
        employee.directs = associates

        self.employees.append(employee)
