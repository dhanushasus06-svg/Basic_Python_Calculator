#Basic_Python_Calculator 

Number_1 = float(input("Enter the first number : "))        
Number_2 = float(input("Enter the second number : "))
Operator = input("Enter any of the listed operator(+,_,*,/) : ")

if Operator == "+" :
    print("Output(Addition) : ", Number_1+Number_2)
elif Operator == "-" :
    print("Output(Substraction) :", Number_1-Number_2)
elif Operator == "*" :
    print("Output(Multiplication) :", Number_1*Number_2)
elif Operator == "/" :
    if(Number_2!=0):
        print("Output(Divsion) :", Number_1/Number_2)
    else:
        print(f"{Number_1}/{Number_2} is not divisible")
else:
    print("Invalid Operator")

    


