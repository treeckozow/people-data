from Person import Person

class Employee(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self._occupation = input("Occupation: ")
        self._salary = input("Salary: ")

    def getOccupation(self):
        return self._occupation
    
    def getSalary(self):
        return self._salary
    
    def getDataDict(self, data_dict):
        data_dict = super().getDataDict(data_dict)
        data_dict["occupation"] = self.getOccupation()
        data_dict["salary"] = self.getSalary()
        return data_dict
    
    def printMyself(self):
        print("Occupation: " + str(self.getOccupation()))
        print("Salary: " + str(self.getSalary()))

    def printPersonData(self):
        super().printPersonData()
        self.printMyself()