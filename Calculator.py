def addition(a, b):
    return print(f"{a} + {b} = {a + b}")

def subtraction(a, b):
    return print(f"{a} - {b} = {a - b}")

def multiplication(a, b):
    return print(f"{a} x {b} = {a * b}")

def division(a, b):
    return print(f"{a} / {b} = {a / b}")



print("===================== Python Calculator =====================")

print("select the desired operation: ")

print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

choice = int(input("enter your option(1/2/3/4): "))

if choice == 0 or choice >= 5:
    print("Opção inválida")
else:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    if choice == 1:    
     addition(n1, n2)
    elif choice == 2:    
        subtraction(n1, n2)
    elif choice == 3:
        multiplication(n1, n2)
    else:
        division(n1, n2)
