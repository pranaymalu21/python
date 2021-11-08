print("Hi how are you today, welcome to my calculator")
print("'+' means addition\n'-' means subtraction\n'/' means divide\n'*' means multiplication\n'^' means square")
operation=input("what would you like to do? '+','-','/','*','^'")
if operation=="+":
    sum1=int(input("enter your first number"))
    sum2=int(input("enter your second number"))
    ans= sum1+sum2
    print(f"your answer is {ans}")
elif operation=="-":
    sum1=int(input("enter your first number"))
    sum2=int(input("enter your second number"))
    ans=sum1 - sum2
    print(f"your answer is {ans}")
elif operation=="/":
    sum1=int(input("enter your first number"))
    sum2=int(input("enter your second number"))
    ans=sum1/sum2
    print(f"your answer is {ans}")
elif operation=="*":
    sum1=int(input("enter your first number"))
    sum2=int(input("enter your second number"))
    ans=sum1*sum2
    print(f"your answer is {ans}")
elif operation=="^":
    sum1=int(input("enter number"))
    ans=sum1*sum1
    print(f"square is {ans}")
else:
    print("invalid")