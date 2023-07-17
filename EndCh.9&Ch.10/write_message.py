filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("This line of code should be on a different line.\n")
    file_object.write("It's ya boy Xzibit! And I'm here to pimp your ride!\n")

#To write code on different lines we have to use the "\n" function every time.
#If you don't the code will be on the same line smushed together. :(

#When you open files with the append function you don't erase all the contents of the file object when opening.
#You have to press run in VS code to have your code appear in the text file.
#Im glad I didn't execute before because I would have deleted my entire file.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding the meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
