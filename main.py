import json
from programmer.company import Company
from programmer.handler_factory import EmployeeFactory

if __name__ == '__main__':
    # c = kindergarden.company.Company()
    # c = intern.company.Company()
    # c = experienced_intern.company.Company()
    company = Company()
    employee_factory = EmployeeFactory.get_hardler()

    with open("csaba_co.json", 'r') as db:
        employees = json.loads(db.read())

    for row in reversed(employees):
        company.add_new_employee(employee_factory.from_row(row, company))
    print(company)
