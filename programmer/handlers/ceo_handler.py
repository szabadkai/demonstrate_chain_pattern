from emp_types import CEO
from programmer.handlers.handler import Handler


class CEOHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == 'CEO':
            employee = CEO(**data)
            employee.associates = [employee.name for employee in company.employees if employee.is_senior]
            employee.salary = company.base_salary * 5 * max([len(company.employees), 1])

            return employee
        return False
