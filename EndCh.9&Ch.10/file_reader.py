with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
# To get rid of the blank line that appears after the file we have to print a certain way. Check it out.

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

# You can use a for loop on the file object to examine each line from a file one at a time. 
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)