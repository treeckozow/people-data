from Person import Person

class Student(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self._subject = input("Subject: ")
        self._year_of_study = input("Year of Study: ")
        self._student_avg = input("Student average: ")

    def getSubject(self):
        return self._subject

    def getYearOfStudy(self):
        return self._year_of_study
    
    def getStudentAvg(self):
        return self._student_avg
    
    def getDataDict(self, data_dict):
        data_dict = super().getDataDict(data_dict)
        data_dict["subject"] = self.getSubject()
        data_dict["Year of Study"] = self.getYearOfStudy()
        data_dict["Student average"] = self.getStudentAvg()
        return data_dict

    def printMyself(self):
        print("Subject: " + str(self.getSubject()))
        print("Year of Study: " + str(self.getYearOfStudy()))
        print("Student average: " + str(self.getStudentAvg()))

    def printPersonData(self):
        super().printPersonData()
        self.printMyself()
