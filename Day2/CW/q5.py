inp_no = input("Enter the numbers")
numbers_list = inp_no.split()

max = int(numbers_list[0])
min = int(numbers_list[0])

for no in numbers_list:
    if(int(no)>max):
        max = int(no)

    if(int(no)<min):
        min = int(no)

with open('minmax_data.txt','w') as output_file:
    output_file.write(f"List: {numbers_list}\n")
    output_file.write(f"Maximum: {max}\n")
    output_file.write(f"Minimum: {min}\n")

with open('minmax_data.txt','r') as input_file:
    print(input_file.readline())
    print(input_file.readline())
    print(input_file.readline())