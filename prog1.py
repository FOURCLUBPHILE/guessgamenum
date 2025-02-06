#Making calculator because i am weak in calculation...just kidding___
x1=int(input("Enter Your First Number: "))
y=(input("Enter the Operator:(+, -, *, /): "))
x2=int(input("Enter Your Second Number: "))

def add(x1,x2):
    return x1+x2
    

def subtracts(x1,x2):
    return x1-x2
    
def multiply(x1,x2):
    return x1*x2
   

def division(x1,x2):
    if x2==0:
        return "ERROR:you cannot divide by zero"
    return x1/x2 or x2/x1
    print(result)


if y=="+":
    result=add(x1,x2)
elif y=="-":
    result=subtracts(x1,x2)
elif y=="*":
    result=multiply(x1,x2)
elif y=="/":
    result=division(x1,x2)
else:
        result="ERROR:YOU HAVE MADE A MISTAKE"
print("RESULT:",result)

