class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Name deleted!')

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)


emp_1 = Employee('Jhon', 'Smith')

emp_1.first = 'Jim'

emp_1.fullname = 'Darth Vader'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname