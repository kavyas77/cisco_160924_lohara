import json

def combined_operations():
    #step 1:Get a list of integers from the user
    user_input = input("Enter at least 5 integers (separated by spaces): ")
    int_list = list(map(int, user_input.split()))

    #step 2: Convert the list to a tuple and display it
    int_tuple = tuple(int_list)
    print(f"Integer list: {int_list}")
    print(f"Integer tuple: {int_tuple}")

    #step 3: Convert the list to a set and remove any duplicates
    int_set = set(int_list)
    print(f"Converted into integer set (removing duplicate elements):{int_set}")

    #step 4:Convert the set to frozenset and display it
    int_frozenset = frozenset(int_set)
    print(f"Converted frozenset:{int_frozenset}")

    #step 5:Create a dictionary where the keys are integers and the values are their squares
    square_dict = {num: num ** 2 for num in int_frozenset}
    print(f"Dictionary of squares: {square_dict}")

    #step 6:Write the dictionary to a JSON file
    with open('squares.json','w') as file:
        json.dump(square_dict, file)
        print("Writing dictionary to file...")

    #Step 7: Reading the file and print its contents
    print("Reading the file...")
    with open('squares.json','r') as file:
        data = json.load(file)
        print(data)

combined_operations()






