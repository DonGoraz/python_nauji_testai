class EmployeeScanner:


    def __init__(self, file_path):
        self.file_path = file_path


    def execute(self):
        pass


    @property
    def employee(self):
        return self.execute()


scanner = EmployeeScanner(company_employees.json)
