from emp_types import Employee
from programmer.handlers.handler import Handler


class DefaultHandler(Handler):

    def _handle(self, data, company):
        employee = Employee(**data)
        employee.salary = company.base_salary

        return employee
