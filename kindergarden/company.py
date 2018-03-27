from employee import Employee


class Company(object):

    employees = []
    base_salary = 2

    def add_new_employee(self, data):
        """
        :param data:
        :return:
        """

        title = data['title']
        age = data['age']
        employee = Employee(**data)

        if title == 'CEO':
            employee.directs = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'senior partner', self.employees))
            employee.compensation_package = ['free money', 'cafeteria', '+1 free day']

            car = 'Bentley Coupe'
            if age > 50:
                car = 'Rolls Royce'

            employee.car = car
            employee.salary = self.base_salary * 5 * max([len(self.employees), 1])

        elif title == 'Senior partner':
            employee.salary = self.base_salary * 5 * max([len(self.employees), 1]) * 0.80
            employee.compensation_package = ['cafeteria', '+1 free day']

            car = 'VW Passat'
            if employee.salary < 20:
                car = 'VW Jetta'

            employee.car = car
            employee.directs = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'junior partner', self.employees))

        elif title == 'Junior partner':
            employee.salary = self.base_salary * 3
            employee.compensation_package = ['+1 free day']
            employee.car = 'VW Jetta'
            employee.directs = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'minion', self.employees))

        else:
            employee.salary = self.base_salary

        self.employees.append(employee)

