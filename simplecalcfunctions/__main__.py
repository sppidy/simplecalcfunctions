print("You Have Imported Simple Calculation Module")

def add(a,b):
    c=a+b
    print(f"The Sum of {a} and {b} is {c}")
def sub(a,b):
    c=a-b
    print(f"The Difference of {a} and {b} is {c}")
def mul(a,b):
    c=a*b
    print(f"The Product of {a} and {b} is {c}")
def div(a,b):
    c=a/b
    print(f"The Quotient of {a} and {b} is {c}")
def rem(a,b):
    c=a%b
    print(f"The Remainder of {a} and {b} is {c}")
def exp(a,b):
    c=a**b
    print(f"The Exponential Value of {a} power {b} is {c}")
def feb(n):
    a,b=0,1
    try:
        while a < n:
            print(a,end=" ")
            a,b=b,a+b
        print()
    except TypeError:
        print("Please enter a valid number")
def arm(a):
    try:
        sum=0
        temp=a
        while temp> 0:
            digit = temp % 10
            sum += digit ** 3
        temp //= 10
        if a == sum:
            print(a,"is an Armstrong Number")
        else:
            print(a,"is not an Armstrong Number")
    except TypeError:
        print("Please enter a valid number")
def helpcalc(help):
    if help=="add":
        print("This function adds two numbers")
    elif help=="sub":
        print("This function subtracts two numbers")
    elif help=="mul":
        print("This function multiplies two numbers")
    elif help=="div":
        print("This function divides two numbers")
    elif help=="rem":
        print("This function finds the remainder of two numbers")
    elif help=="exp":
        print("This function finds the exponential value of two numbers")
    elif help=="feb":
        print("This function finds the nth number in the fibonacci series")
    elif help=="arm":
        print("This function checks if a number is an Armstrong number")
    else:
        print("Please enter a valid command")
