import json
class patientmanagementlist:
    def __init__(self):
        self.patients=[]
    def add_patient(self,name):
        if name not in self.patients:
            self.patients.append(name)
            print(f"Patient {name} added successfully.")
        else:
            print(f"Patient {name} already exists.")


    def remove_patient(self,name):
        if name in self.patients:
            self.patients.remove(name)
            print(f"Patient {name} removed successfully.")
        else:
            print(f"Patient {name} does not exist.")
    def display_patients(self):
        if self.patients:
            print("Current list of patients:")
            for i,patient in enumerate(self.patients, 1):
                print(f"{i}. {patient}")
        else:
            print("No patients in the list.")


def write_to_json(self,filename):
    with open('filename', 'w') as file:
        json.dump(self.patients, file)
        print(f"Patient list written to {filename}.")


def main_list():
    management = patientmanagementlist()
    while True:
        print("\nPatient Management System (List)")
        print("1. Add patient")
        print("2. Remove patient")
        print("3. Display patients")
        print("4. Write to JSON")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter patient name to add: ")
            management.add_patient(name)
        elif choice == '2':
            name = input("Enter patient name to remove: ")
            management.remove_patient(name)
        elif choice == '3':
            management.display_patients()
        elif choice == '4':
                filename = input("Enter the filename to write to (e.g., patients_list.json): ")
                management.write_to_json(filename)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_list()

