class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def getDataDict(self, data_dict):
        data_dict = {"id": self.getId(), "name": self.getName(), "age": self.getAge()}
        return data_dict

    def printPersonData(self):
        print("ID: " + str(self.getId()))
        print("Name: " + str(self.getName()))
        print("Age: " + str(self.getAge()))
    
if __name__ == "__main__":
    id_test = 54321
    name_test = "Dan"
    age_test = 31
    person = Person(id_test, name_test, age_test)
    if person.getId() != id_test:
        print("Error: the ID you got is " + str(person.getId()) + " but it should be " + str(id_test))
    if person.getName() != name_test:
        print("Error: the Name you got is " + str(person.getName()) + " but it should be " + str(name_test))
    if person.getAge() != age_test:
        print("Error: the Age you got is " + str(person.getAge()) + " but it should be " + str(age_test))