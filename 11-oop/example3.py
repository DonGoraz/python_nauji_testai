class Workers:
    existingWorkers = ["Tadas", "Tomas", "Mindaugas", "Karolis"]
    def __init__(self, name):
        self._name = ""
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, nameEntered):
        if nameEntered not in self.existingWorkers:
            print(f"Worker with name {nameEntered} doesn't work for the company")
        else:
            self._name = nameEntered
worker1 = Workers("Tadas")
print(worker1.name)