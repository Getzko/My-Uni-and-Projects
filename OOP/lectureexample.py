class Employee:
    company_name='hamk'
    employee_count=0

    @classmethod
    def set_company_name(cls,name):
        cls.company_name=name

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.employee_count+=1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary must be greater than 0.")
        self._salary=value
    def calculate_tax(self):
        salary = self.salary
        if salary < 2000:
            return salary
        elif salary < 4000:
            return salary * 0.2
        else: return salary * 0.3
    def display(self):
        print("Employee Name:", self.name)
        print("Salary before tax:", self.salary)
        print("Tax:", self.calculate_tax())
        print("Company:", self.company_name)

employee1=Employee("John",3000)
Employee.set_company_name('mcdonalds')
employee1.display()
print("Total Employees:", Employee.get_employee_count)
