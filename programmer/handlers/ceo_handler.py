from emp_types import CEO
from programmer.handlers.handler import Handler
from ..tittles import TITTLES

class CEOHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == TITTLES.ceo:
            employee = CEO(**data)

            employee.directs = [x.name for x in company.employees if x.title == TITTLES.senior_partner]
            employee.salary = company.base_salary * 5 * len(company.employees)

            return employee
        return False
