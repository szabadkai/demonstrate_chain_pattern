from emp_types import Senior
from programmer.handlers.handler import Handler


class SeniorHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == 'Senior partner':
            employee = Senior(**data)

            employee.associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'junior partner', company.employees))
            employee.salary = company.base_salary * 5 * max([len(company.employees), 1]) * 0.80
            employee.car = 'VW Passat' if employee.salary > 20 else 'VW Jetta'

            return employee
        return False
