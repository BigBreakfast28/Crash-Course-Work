try: 
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#This is a dope ass way to counter errors that you anticipate happening inside of your program.
#If more code followed the 'try-except' block then the code would continue to run without any problem. 

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit!")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)