import json
import re
from app_code.database import *


class EmployeeScanner:

    def __init__(self, first_name: str, last_name: str,  role: int, annual_salary: float, feedback: int, years_employed: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.years_employed = years_employed
        self.email = email
        self.feedback = feedback
        self.role = role

    def __str__(self):  # naudojamas kai objekta kvieciame su print() funkcija
        return f"'{self.first_name}', '{self.last_name}', '{self.role}', {self.annual_salary}, {self.feedback}, {self.years_employed}, '{self.email}'"

    @classmethod
    def create_from_string(cls, employee_str: str):
        first_name, last_name, role, annual_salary, feedback, years_employed, email = employee_str.split(",")
        annual_salary, years_employed, feedback = float(annual_salary), int(years_employed), int(feedback)
        if cls.is_email_correct(email):
            if not (check_if_employee_exists(email)):
                create_employee(first_name, last_name, role, annual_salary, feedback, years_employed, email)
            return cls(first_name, last_name, role, annual_salary, feedback, years_employed, email)

    @staticmethod
    def is_email_correct(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        else:
            return False


create_employee_table()
get_employees()

with open("company_employees.json", "r") as read_file1:
    data1 = json.load(read_file1)

with open("feedback_for_employees.json", "r") as read_file2:
    data2 = json.load(read_file2)

x = lambda a: a >= 3
for _ in data1["Employees"]:
    if x(_['years_employed']):
        for el in data2["Feedback"]:
            if _['emailAddress'] == el['emailAddress']:
                EmployeeScanner.create_from_string(f"{_['firstName']},{_['lastName']},{el['role']},{_['annual_salary']},{el['feedback']},{_['years_employed']},{_['emailAddress']}")

get_employees()
