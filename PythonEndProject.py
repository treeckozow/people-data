import os
import pandas as pd
from Person import Person
from Employee import Employee
from Student import Student
from Menu import Menu

def getMenuOption():
    for option in Menu:
        print("type '" + str(option.value) + "' to " + option.name)
    return input("Please enter your choice: ")

def saveEntrysAsData(info_list, data_list):
    for person in info_list:
        data_dict = {}
        data_list.append(person.getDataDict(data_dict))
    return data_list

def saveDataAsCsv(info_list, data_list, path):
    output_file = input("What is your output file name? ")
    saveEntrysAsData(info_list, data_list)
    csv_path = os.path.join(path, output_file)
    data_frame = pd.DataFrame(data_list)
    data_frame.to_csv(csv_path, index=False)         

def exitConfirmation():
    while True:
        answer = input("Are you sure? (y/n)")
        if answer == "n":
            return False
        if answer == "y":
            return True

def getAgesSum(people_data, current_sum):
    current_sum += int(people_data[-1].getAge())
    return current_sum

def notNumError(user_input, key):
    print("Error: " + key + " must be a number. [" + str(user_input) + "] is not a number")

def saveNewEntry(info_dicsh, info_list): # 1
    id = input("ID: ")
    if id in info_dicsh:
        print("Error: ID already exists: " + str(info_dicsh[id]))
        return False 
    if not id.isdigit():
        notNumError(id, "ID")
        return False
    name = input("Name: ")
    age = input("Age: ")
    if not age.isdigit():
        notNumError(age, "Age")
        return False
    while True:
        employ_or_student = input("Is " + name + " an enployee or a student (for neither type 'n'): ")
        if employ_or_student == "n":
            new_person = Person(id, name, age)
            break
        elif employ_or_student == "employee":
            new_person = Employee(id, name, age)
            break
        elif employ_or_student == "student":
            new_person = Student(id, name, age)
            break
    info_list.append(new_person)
    info_dicsh[id] = new_person
    print("ID [" + str(id) + "] saved successfuly")
    return True

def searchById(info_dicsh): #3
    id_to_search = input("Please enter the ID you want to look for: ")
    try:
        info_dicsh[id_to_search].printPersonData()
    except:
        print("An Error has occurred please try again")

def printAllEntrys(info_list):
    for idx, entry in enumerate(info_list):
        print(str(idx) + ". ")
        entry.printPersonData()

def printAgesAvg(sum, people_amount):
    ages_avg = sum / people_amount
    print(ages_avg)

def printAllNames(info_list):
    for idx, name in enumerate(info_list):
        print(str(idx) + ". " + name.getName())

def printAllIds(info_list):
    for idx, id in enumerate(info_list):
        print(str(idx) + ". " + id.getId())

def printEntryByIndex(info_list):
    idx = input("Please enter the index of the entry you want to print: ")
    try:
        idx = int(idx)
    except ValueError:
        notNumError(idx, "Index")
        return
    try:
        info_list[idx].printPersonData()
    except IndexError:
        print("IndexError: list index out of range. the maximum index allowed is " + str(len(info_list) - 1))

id_list = []
id_dicsh ={}
ages_sum = 0
main_path = "C:\\Users\\treec\\Desktop\\forward\\Python\\projects\\advanced\\end project"

while True:
    try:
        choice = getMenuOption()
        try:
            choice = Menu(int(choice))
        except ValueError:
            if not choice.isdigit():
                notNumError(choice, "choice")
            else:
                print("Error: Option [" + str(choice) + "] is out of range. Please try again")
            continue
        if choice == Menu.SAVE_NEW_ENTRY:
            if saveNewEntry(id_dicsh, id_list):
                ages_sum = getAgesSum(id_list, ages_sum)
        elif choice == Menu.SEARCH_ENTRY_BY_ID:
            searchById(id_dicsh)
        elif choice == Menu.PRINT_AGES_AVERAGE:
            try:
                printAgesAvg(ages_sum, len(id_list))
            except ZeroDivisionError:
                print("Error: division by zero")
        elif choice == Menu.PRINT_ALL_NAMES:
            printAllNames(id_list)
        elif choice == Menu.PRINT_ALL_IDS:
            printAllIds(id_list)
        elif choice == Menu.PRINT_ALL_ENTRYS:
            printAllEntrys(id_list)
        elif choice == Menu.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex(id_list)
        elif choice == Menu.SAVE_ALL_DATA:
            people_data_list = []
            try:
                saveDataAsCsv(id_list, people_data_list, main_path)
            except FileNotFoundError:
                print("Error: File not found")
        elif choice == Menu.EXIT:
            if exitConfirmation():
                print("Goodbye!")
                break
        input("Press Enter to continue ")
    except KeyboardInterrupt:
        print("\nError: Keyboard interrupt")