from employee import Employee


class CEO(Employee):

    def __init__(self, name, title, age):
        super(CEO, self).__init__(name, title, age)

        self.compensation_package = ['free money', 'cafeteria', '+1 free day']

        car = 'Bentley Coupe'
        if age > 50:
            car = 'Rolls Royce'

        self.car = car


class Senior(Employee):

    def __init__(self, name, title, age):
        super(Senior, self).__init__(name, title, age)

        self.compensation_package = ['cafeteria', '+1 free day']


class Junior(Employee):

    def __init__(self, name, title, age):
        super(Junior, self).__init__(name, title, age)

        self.compensation_package = ['+1 free day']
        self.car = 'VW Jetta'