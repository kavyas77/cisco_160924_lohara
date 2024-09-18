from patient import Patient
patients = {}
    
def patient_add(id,name):
    global patients
    patient = Patient(id,name)
    patients[patient.id]=patient
    print('patient created sucessfully')

def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient== None:
            print(f'No such id {id}')
            return
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                del patients[id]
                print('Patient deleted successfully')
            
    

def patient_update(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    name = input(f'enter new name({patient.name}):')
    patient.name =name
    print('patient updated successfully')


def patient_display():
    global patients
    for id in patients:
        print(patients[id])

def patient_display_by_id(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    