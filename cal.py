
def calculator():
    a=float(input("Enter the first number"))
    b=float(input("Enter the second number"))
    c=input("Enter the operation symbol")
    if c=="+":
        return (a+b)
    elif c=="-":
        return abs(a-b)
    elif c=="*":
        return (a*b)
    elif c=="/":
        if b==0:
           return("the value is invalid")
        else:
            return (a/b)
    elif c=="%":
        if b==0:
            return("the value is invalid")
        else:
            return (a%b)
    elif c=="**":
        return(a**b)
    else:
        return("try again")
        
print(calculator())
