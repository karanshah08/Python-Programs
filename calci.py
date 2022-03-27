a = int(input("Enter a :"))
b = int(input("Enter b :"))
operator = input("Select an operator (+,-,/,*,%) : ")

if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)    
elif operator == "/":
    print(a/b) 
elif operator == "*":
    print(a*b)
elif operator == "%":
    print(a%b) 
else:
    print("Invalid Operator")

print("Above is your answer")              
