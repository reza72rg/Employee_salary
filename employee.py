class Employee:
    salary = 3000
    total_employee = 0

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        Employee.total_employee += 1

    def fullname(self):
        return f'{self.name} {self.lastname}'

    @classmethod
    def raise_salary(cls, new_salary):
        """
        Class method to raise the salary of all employees.
        """
        if isinstance(new_salary, int):
            cls.salary = new_salary
        else:
            raise ValueError("Salary must be an integer.")

    @classmethod
    def create_from_string(cls, string):
        """
        Class method to create an Employee instance from a string in the format 'name-lastname'.
        """
        name, lastname = string.split('-')
        return cls(name, lastname)

    @staticmethod
    def is_workday(day):
        """
        Static method to check if a given day is a workday (Monday to Friday).
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Create an Employee instance using the create_from_string class method
emp3 = Employee.create_from_string('reza-latifi')

# Import the datetime module and create a date object
import datetime
date = datetime.date.today()

# Check if the given date is a workday using the is_workday static method
print(emp3.is_workday(date))

# Create two Employee instances using the __init__ method
emp1 = Employee('reza', 'latifi')
emp2 = Employee('javad', 'abasi')

