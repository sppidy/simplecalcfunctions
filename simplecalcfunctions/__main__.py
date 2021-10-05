def helpme(n):
    if n=="help":
        print("The following commands are available : add\nsub\nmul\ndiv\nrem\nexp\nfeb\narm\nstarpat\nFor a detailed Help try helpcalc(function_name)")
    else:
        print("Please enter a valid command")
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
    try:
        a,b=0,1
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
def starpat(n):
    try:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    except TypeError:
        print("Please enter a valid number")
def lcm(x,y):
    try:
        if x>y:
            z=x
        else:
            z=y
        while True:
            if z%x==0 and z%y==0:
                lcm=z
                break
            z+=1
        print(f"The LCM of {x} and {y} is {lcm}")
    except TypeError:
        print("Please enter a valid number")
def hcf(x,y):
    try:
        if x>y:
            z=x
        else:
            z=y
        while True:
            if z%x==0 and z%y==0:
                hcf=z
                break
            z-=1
        print(f"The HCF of {x} and {y} is {hcf}")
    except TypeError:
        print("Please enter a valid number")
def sqrt(n):
    try:
        if n<0:
            print("Please enter a valid number")
        else:
            x=n
            while True:
                y=(x+n/x)/2
                if y==x:
                    break
                x=y
            print(f"The Square root of {n} is {x}")
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
    elif help=="starpat":
        print("This function prints a pattern of stars")
    else:
        print("Please enter a valid command")
