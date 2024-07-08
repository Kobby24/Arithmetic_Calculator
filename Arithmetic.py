



#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

#Multiply
def mul(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2
#clear 
def clear():
    print("\n" *100)
operations = {
    "+" : add, 
    "-" : sub, 
    "*" : mul, 
    "/" : div
}
def calculator():

    num1 = float(input("Enter the First number: "))

    for symbol in operations:
        print(symbol)
    value = True
    while value:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)



        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_now = input("Do you want to continue with the answer. Yes or No: ").lower()
        if continue_now == "yes":
            num1 = answer
            value = True
        else:
            value = False
            clear()
            calculator()
calculator()