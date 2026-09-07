class Employee:
    def __init__(self, name, department, salary, employee_id):
        self.name=name
        self.department=department
        self.__salary=salary
        self.__employee_id=employee_id #employee id should be private, becausee .....
    def taxfraud(self):
        change=input("Add money ")
        self.__salary+=change
        print


emp1=Employee("sara","IT",4500,23222)
print(emp1.name)
print(emp1.department)
print(emp1.department)
emp1._Employee__salary = 600000
print(emp1._Employee__salary)
