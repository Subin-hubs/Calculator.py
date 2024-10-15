def show_menu():
    print("Enter your choice")
    print("Select 1 for the Sum of a number")
    print("Select 2 for the diffrence of a number")
    print("Select 3 for the division of a number")
    print("Select 4 for the multiplication of a number")
    print("Select 5 for EXIST")

def Sum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    Sum=num1+num2
    print(f"The sum of the given number is {sum}")
    
def Diffrence():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    Diffrence = num1-num2
    print(f"The diffrence of a given number is {Diffrence}")
    
def multiplication():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    multiplication = num1*num2
    print(f"The multiplication of the given number is {multiplication}")
    
def division():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    division = num1/num2
    print(f"The divison of the given number is {division}")
    
def lost():
    print("Get lost")
    
while True:
    
    show_menu()
    choice = int(input("Enter a number: "))
    
    if choice == 1:
        sum()
        
    elif choice ==2:
        Diffrence()
        
    elif choice == 3:
        multiplication()
        
    elif choice == 4:
        division()
        
    elif choice == 5:
        lost()
        
    else:
        break