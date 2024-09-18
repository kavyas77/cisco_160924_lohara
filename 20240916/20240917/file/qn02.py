names_list=input('enter student names(separated by spaces):').split()
names_set=set(names_list)
names_fset = frozenset(names_set)
names_dict={name:len(name) for name in names_fset}
print(f'orginal list:{names_list}')
print(f'set (no duplicates):{names_list}')
print(f'frozen Set:{names_set}')
print(f'Dictonary of name lengths:{names_dict}')
import json
with open('qn02_data.json','w') as names_db:
    json.dump(names_dict, names_db)
print('Dictionary written to JSON file.')
with open('qn02_data.json','r') as names_db:
    names_dict2=json.load(names_db)
    print(f'Reading from JSON file...\n{names_dict2}')