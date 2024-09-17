patients = []
def patient_add(patient):
    patients.append(patient)
    print("the patient {} is added successfully".format(patient))


def patient_delete(patient):
    try:
        patients.remove(patient)
        print("the patient {} is removed successfully".format(patient))
    except ValueError as err:
        print('No such patient')

def display_patients():
    if patients:
        print(patients)
    else:
        print("No patients in the list")
    

def menu():
    choice = int(input('''1-add
2-delete
your choice:'''))
    if choice == 1:
        patient = input('Enter patient name:')
        patient_add(patient)
    elif choice == 2:
        patient = input('Enter patient name:')
        patient_delete(patient)
    
        

def menus():
    choice = menu()
    while choice != 3:
        choice = menu()
        display_patients()1
    print('App Ended')

menus()