inp = input("Enter the numbers")
inpvar = inp.split()
list_num = list(inpvar)
sum = 0
for no in list_num:
    sum += int(no)
avg = sum/len(list_num)
with open('numbers_data.txt','w') as output_file:
    output_file.write(f"List: {list_num}\n")
    output_file.write(f"Sum: {sum}\n")
    output_file.write(f"Average: {avg}\n")
    output_file.close()

with open('numbers_data.txt','r') as input_file:
    print(input_file.read())
    print(input_file.read())
    print(input_file.read())
    input_file.close()