import json

class Patient:
    def __init__(self,id,name):
        self.id =  id
        self.name = name

    def from_dict(cls, data):
        return cls(data['id'],data['name'])
    def to_dict(self):
        return {'id': self.id, 'name': self.name}
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()
    
patients = []


   
def patient_add(id,name):
    global patients
    patient = Patient(id,name)
    patients.append(patient)

def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully')
            return 
    print(f'No such id {id}')

def patient_display():
    global patients
    for patient in patients:
        print(patient)

def save_patient_to_json(file_path):
    with open(file_path, 'w') as file:
        json.dump([p.to_dict() for p in patients], file, indent=4)

def load_patients_from_json(file_path):
    global patients
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            patients = [Patient.from_dict(p) for p in data]
    except FileNotFoundError:
        print(f"No file found at {file_path}. Starting with an empty list.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty list.")


def menu():
    choice = int(input('''1-add patient
2-delete patient by id
3-display all patients
4-save to file
5-load from file
7-end
your choice:'''))
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('enter patient name:')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to remove:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice ==4:
        file_path = input('Enter filename to save: ')
        save_patient_to_json(file_path)
    elif choice == 5:
        file_path = input('Enter filename to load: ')
        load_patients_from_json(file_path)

    elif choice == 7:
        pass 
    else:
        print('Invalid menu')
    return choice
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')
        
menus()


