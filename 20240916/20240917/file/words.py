words_list=input('enter words (seperated by space):').split()
int_list=(int(n) for n in words_list)
words_tuple=tuple(words_list)
print(f'List:{words_list}')
print(f'Tuple:{words_list}')
with open('words.txt','w')as data_file:
    data_file.write(f'List:{words_list}\n')
    data_file.write(f'Tuple:{words_list}')
print('Data written to file')
with open('words.txt','r')as data_file:
    line_list=data_file.readline()
    line_tuple=data_file.readline()
    print(line_list)
    print(line_tuple)



