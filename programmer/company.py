from programmer.handlers.ceo_handler import CEOHandler
from programmer.handlers.default_handler import DefaultHandler
from programmer.handlers.junior_handler import JuniorHandler
from programmer.handlers.senior_handler import SeniorHandler


class HandlerFactory(object):

    @classmethod
    def generate(cls, handlers):
        if handlers:
            return handlers.pop(0)(cls.generate(handlers))


class Company(object):

    employees = []
    base_salary = 2

    def __init__(self):
        # it could be hard to maintain the chain, i prefer to define a factory to create the chain.
        # self.handler = CEOHandler(SeniorHandler(JuniorHandler(DefaultHandler())))

        self.handler = HandlerFactory.generate([
            CEOHandler,
            SeniorHandler,
            JuniorHandler,
            DefaultHandler
        ])

    def add_new_employee(self, data):
        """
        :param data: { 'name': str, 'age': int, 'title': str }
        :return:
        """

        employee = self.handler.handle(data, Company)
        self.employees.append(employee)
