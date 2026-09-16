numb1=int(input("enter first number"))
numb2=int(input("enter second number"))
operator=input("enter operator")
if operator=="+":
    print(numb1+numb2)
elif  operator=="-":
    print(numb1-numb2)
elif operator=="*":
    print(numb1*numb2)
elif operator=="/":
    print(numb1/numb2)
else:
    print("Operator not supported")
