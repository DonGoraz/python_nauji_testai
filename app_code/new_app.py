import json

from app_code.database import *
# from database import DatabaseContextManager

class EmployeeScanner():

    def __init__(self, *args):
        self.file1 = args[0]
        self.file2 = args[1]

    def execute(self):

        with open(self.file1, "r") as read_file1:
            with open(self.file2, "r") as read_file2:
                data1 = json.load(read_file1)
                print(type(data1["Employees"]))
                data2 = json.load(read_file2)
                print(data2["Feedback"])
                print("-"*50)

    @property
    def employee(self):
        return self.execute()


scanner = EmployeeScanner("company_employees.json", "feedback_for_employees.json")
# scanner.employee


create_employee_table()