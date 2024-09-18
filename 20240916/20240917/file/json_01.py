import json
patients = [
    {'id':101, 'Name':'mahesh'},
    {'id':102, 'Name':'dravid'},
    {'id':103, 'Name':'rohit'},
]
patients_str = json.dumps(patients)
print(patients,patients_str)
with open('patients_data.json','w') as patients_db:
    json.dump(patients,patients_db)

with open('patients_data.json','r') as patients_db:
    patient_list3=json.load(patients_db)
    print(patient_list3,type(patient_list3))


patients_list2 = json.loads(patients_str)
print(patients_list2, type(patients_list2))