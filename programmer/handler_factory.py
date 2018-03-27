from programmer.handlers.ceo_handler import CEOHandler
from programmer.handlers.default_handler import DefaultHandler
from programmer.handlers.junior_handler import JuniorHandler
from programmer.handlers.senior_handler import SeniorHandler


class EmployeeFactory(object):

    @staticmethod
    def get_hardler():
        return CEOHandler(SeniorHandler(JuniorHandler(DefaultHandler())))