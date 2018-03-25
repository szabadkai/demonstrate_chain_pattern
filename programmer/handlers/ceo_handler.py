from emp_types import CEO
from programmer.handlers.handler import Handler


class CEOHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == 'CEO':
            employee = CEO(**data)

            employee.associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'senior partner', company.employees))
            employee.salary = company.base_salary * 5 * max([len(company.employees), 1])

            return employee
        return False
