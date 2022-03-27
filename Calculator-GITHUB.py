number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2 : "))

operator = input("Select an opeartor ('+','-','/','*','%')")

if operator == '+' :
    print("The Answer is ",number1+number2)
elif operator == '-' :
    print("The Answer is ",number1-number2)
elif operator == '/' :
    print("The Answer is ",number1/number2)
elif operator == '*' :
    print("The Answer is ",number1*number2)
elif operator == '%' :
    print("The Answer is ",number1%number2)
else:
    print("The operator u have chosen is Invalid :)")
