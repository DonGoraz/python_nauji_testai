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
            if not(check_if_employee_exists(email)):
                create_employee(first_name, last_name, role, annual_salary, feedback, years_employed, email)
                return print(f"Create New Employee\n {first_name}\n {last_name}\n {role}\n {annual_salary}\n {feedback}\n {years_employed}\n {email}\n")

    @staticmethod
    def is_email_correct(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        else:
            return False


def get_file_info(fname):
    with open(fname, "r") as read_file:
        data = json.load(read_file)
        return data


create_employee_table()
data1 = get_file_info("company_employees.json")
data2 = get_file_info("feedback_for_employees.json")

x = lambda x: x >= 3  # Lambda usage for filtering Employee less than 3 years of work experience
for _ in data1["Employees"]:
    if x(_['years_employed']):
        for el in data2["Feedback"]:
            if _['emailAddress'] == el['emailAddress']:
                EmployeeScanner.create_from_string(f"{_['firstName']},{_['lastName']},{el['role']},{_['annual_salary']},{el['feedback']},{_['years_employed']},{_['emailAddress']}")
                break

get_employees()
