from patient_service import patient_add, patient_display, patient_display_by_id
from patient_service import patient_update, patient_remove
def menu():
    choice = int(input('''1-add patient
2-delete patient by id
3-display all patients
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