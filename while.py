c="y"
while c == "y":
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    operator=input("enter the symbol:")
    match operator:
        case '+':
            print(f"sum is{num1+num2}")
        case '-':
            print(f"substraction is{num1-num2}")
        case '*':
            print(f"multiplication is{num1*num2}")
        case '/':
            print(f"divison is{num1/num2}")
        case _:
            print("syntax error")
    c=input("do you want to continue  ")
            
