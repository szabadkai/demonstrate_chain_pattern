from emp_types import Junior
from programmer.handlers.handler import Handler


class JuniorHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == 'Junior partner':
            employee = Junior(**data)

            employee.associates = map(lambda x: x.name, filter(lambda x: x.title.lower() == 'minion', company.employees))
            employee.salary = company.base_salary * 3

            return employee
        return False
