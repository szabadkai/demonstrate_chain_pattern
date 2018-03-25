from employee import Employee


class Company(object):

    employees = []
    base_salary = 2

    def ceo(self, age):
        associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'senior partner', self.employees))
        compensation_package = ['free money', 'cafeteria', '+1 free day']

        car = 'Bentley Coupe'
        if age > 50:
            car = 'Rolls Royce'

        salary = self.base_salary * 5 * max([len(self.employees), 1])

        return associates, car, salary, compensation_package

    def senior(self):
        salary = self.base_salary * 5 * max([len(self.employees), 1]) * 0.80
        compensation_package = ['cafeteria', '+1 free day']

        car = 'VW Passat'
        if salary < 20:
            car = 'VW Jetta'

        associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'junior partner', self.employees))

        return associates, car, salary, compensation_package

    def junior(self):
        salary = self.base_salary * 3
        compensation_package = ['+1 free day']
        car = 'VW Jetta'
        associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'minion', self.employees))

        return associates, car, salary, compensation_package

    def add_new_employee(self, data):
        """
        :param data:
        :return:
        """

        title = data['title']
        age = data['age']
        employee = Employee(**data)

        associates = []
        compensation_package = None
        car = None

        if title == 'CEO':
            associates, car, salary, compensation_package = self.ceo(age)

        elif title == 'Senior partner':
            associates, car, salary, compensation_package = self.senior()

        elif title == 'Junior partner':
            associates, car, salary, compensation_package = self.junior()

        else:
            salary = self.base_salary

        employee.salary = salary
        employee.car = car
        employee.compensation_package = compensation_package
        employee.associates = associates

        self.employees.append(employee)
