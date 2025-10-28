import os

while True:

    os.system("cls")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 * num2

    print(f"\n O resultado de {num1} * {num2} é = {resultado}")

    continuar = input("\n Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("\ncabou ate a proxiama")   
        break
    print("-" * 40)

