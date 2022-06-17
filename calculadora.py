def soma(a, b):
    return print(f"{a} + {b} = {a + b}")

def subtracao(a, b):
    return print(f"{a} - {b} = {a - b}")

def multiplicacao(a, b):
    return print(f"{a} x {b} = {a * b}")

def divisao(a, b):
    return print(f"{a} / {b} = {a / b}")



print("===================== Python Calculator =====================")

print("Selecione o número da operação desejada: ")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite sua opção(1/2/3/4): "))

if opcao == 0 or opcao >= 5:
    print("Opção inválida")
else:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if opcao == 1:    
     soma(n1, n2)
    elif opcao == 2:    
        subtracao(n1, n2)
    elif opcao == 3:
        multiplicacao(n1, n2)
    else:
        divisao(n1, n2)