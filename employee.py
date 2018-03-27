class Employee(object):

    def __init__(self, name, title, age):
        self.name = name
        self.title = title
        self.age = age
        self.salary = None
        self.car = None
        self.compensation_package = None
        self.directs = []
