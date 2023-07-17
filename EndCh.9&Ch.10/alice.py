#This file is about writing a try block that accounts for a file that does not exist.
filename = 'alice.txt'

try: 
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else: 
    #Count the approx. number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")