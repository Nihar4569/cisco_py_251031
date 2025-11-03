sentence = input("Enter a sentence: ")
words = sentence.split()
words_list = list(words)
words_upper = [word.upper() for word in words]
words_tuple = tuple(words_upper)

with open('sentence_data.txt','w') as output_file:
    output_file.write(f"List: {words_list}\n")
    output_file.write(f"Tuple: {words_tuple}\n")
    output_file.close()

with open('sentence_data.txt','r') as input_file:
    print(input_file.readline())
    print(input_file.readline())
    input_file.close()
