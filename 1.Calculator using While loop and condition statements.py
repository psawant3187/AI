#defining functions
def add(a,b):
    solnadd= a+b
    print("Solution after Adding two numbers is:",solnadd)

def sub(a,b):
    solnsub = a-b
    print("Solution after Subtracting two numbers is:",solnsub)

def multi(a,b):
    solnmulti = a*b
    print("Solution after Multiplying two numbers is:",solnmulti)

def div(a,b):
    solndiv = a/b
    print("Solution after Dividing two numbers is:",solndiv)

print("WELCOME TO CALCULATOR")

#creating Menu
while True:
    print("\n MAIN MENU")  
    print("1. ADD \n")  
    print("2. SUBTRACT \n")  
    print("3. MULTIPLY \n")  
    print("4. DIVIDE \n") 
    print("5. END \n") 
    choice = int(input("Enter the Choice:")) 

    if choice==1:
        a = int(input("Enter the First Number:"))
        b = int(input("Enter the Second Number:"))
        add(a,b)

    elif choice==2:
        a = int(input("Enter the First Number:"))
        b = int(input("Enter the Second Number:"))
        sub(a,b)

    elif choice==3:
        a = int(input("Enter the First Number:"))
        b = int(input("Enter the Second Number:"))
        multi(a,b)

    elif choice==4:
        a = int(input("Enter the First Number:"))
        b = int(input("Enter the Second Number:"))
        div(a,b)

    elif choice==5:
        break

    else:
        print("Invalid Choice M*****Fucker")