names_input = input("Enter names separated by commas: ")
name_sort = sorted(names_input.split(' '))
name_tuple = tuple(name_sort)

with open('names_data.txt','w') as output_file:
    output_file.write(f"Sorted List: {name_sort}\n")
    output_file.write(f"Tuple: {name_tuple}\n")

with open('names_data.txt','r') as input_file:
    print(input_file.readline())
    print(input_file.readline())