import experienced_intern.company
import kindergarden.company
import intern.company
import programmer.company

if __name__ == '__main__':
    # c = kindergarden.company.Company()
    # c = intern.company.Company()
    # c = experienced_intern.company.Company()
    c = programmer.company.Company()

    employees = [
        {
            'name': 'Csaba I.',
            'age': 25,
            'title': 'CEO'
        },
        {
            'name': 'Some One 1',
            'age': 30,
            'title': 'Senior partner'
        },
        {
            'name': 'Some One 2',
            'age': 30,
            'title': 'Junior partner'
        },
        {
            'name': 'Some One 3',
            'age': 18,
            'title': 'Minion'
        },
        {
            'name': 'Some One 4',
            'age': 19,
            'title': 'Minion'
        }
    ]

    for emp in employees[::-1]:
        c.add_new_employee(emp)

    for emp in c.employees:
        print vars(emp)
