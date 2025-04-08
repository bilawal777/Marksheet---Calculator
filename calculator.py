#   calculator
def calculator (num1,num2,operate):
    if operate == "+":
        return  num1 + num2
    elif operate == "-":
        return  num1 - num2
    elif operate == "*":
        return  num1 * num2
    elif operate == "/":
        if num2 == 0:
            print("Zero Division Error")
            return num1/num2
    else:  
        return "Invalid operation"
# main program
def main():
    print("welcome to my python calculator")
    num1 = float(input ("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print("Select the operator from + ,  - , * , /")
    operate = input("Enter operator: ")
    result = calculator(num1 , num2 , operate)
    print(f"The result of {operate} is : {result}")

main()
