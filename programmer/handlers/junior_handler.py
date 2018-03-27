from emp_types import Junior
from programmer.handlers.handler import Handler
from ..tittles import TITTLES


class JuniorHandler(Handler):

    def _handle(self, data, company):
        if data['title'] == TITTLES.junior_partner:
            employee = Junior(**data)
            employee.directs = [e.name for e in company.employees if e.title == TITTLES.minion]
            employee.salary = company.base_salary * 3

            return employee
        return False
