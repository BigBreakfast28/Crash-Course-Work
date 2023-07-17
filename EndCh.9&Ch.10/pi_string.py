filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

#We have used a 'with block' to store the information from the file 'pi_digits.txt' as 'lines'.
#Since the information is stored in such a way, we can manipulate the data in a way we normally couldn't.

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))