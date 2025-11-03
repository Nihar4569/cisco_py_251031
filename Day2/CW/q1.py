words_seq = input('Words seperated by space')
print(words_seq)
words = words_seq.split()
print(words, type(words))
word_tuple = tuple(words)
print(word_tuple, type(word_tuple))

output_file = open('qn01_date.txt', 'w')
output_file.write(f"List: {words}\n")
output_file.write(f"Tuple: {word_tuple}\n")
output_file.close()

with open('qn01_date.txt','w') as output_file:
    output_file.write(f"List: {words}\n")
    output_file.write(f"Tuple: {word_tuple}\n")

with open('qn01_date.txt','r') as input_file:
    file_words_list_line = input_file.readline()
    file_words_tuple_line = input_file.readline()
    print(file_words_list_line)
    print(file_words_tuple_line)
