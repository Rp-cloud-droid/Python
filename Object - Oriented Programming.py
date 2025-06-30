class Employee:

    def __init__(self):
        print('Employee Created.')

    def __del__(self):
        print('Destructor called, Employee detected.')

obj = Employee()
del obj