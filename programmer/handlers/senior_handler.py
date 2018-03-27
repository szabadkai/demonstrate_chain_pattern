from emp_types import Senior
from programmer.handlers.handler import Handler
from ..tittles import TITTLES

class SeniorHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == TITTLES.senior_partner:
            employee = Senior(**data)

            employee.directs = [x.name for x in company.employees if x.title == TITTLES.junior_partner]
            employee.salary = company.base_salary * 5 * max([len(company.employees), 1]) * 0.80
            employee.car = 'VW Passat' if employee.salary > 20 else 'VW Jetta'

            return employee
        return False
