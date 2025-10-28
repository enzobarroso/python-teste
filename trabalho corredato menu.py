import os
import math
import random

def raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))   
    if numero < 0:
        print("Número inválido. Não é possível calcular a raiz quadrada de um número negativo.")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("Pressione Enter para continuar...")

def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} elevado a {expoente} é {resultado}")
    input("Pressione qualquer tecla para continuar...")

def numero_aleatorio():
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))
    if inicio > fim:
        print("O valor inicial deve ser menor ou igual ao valor final.")
    else:
        numero = random.randint(inicio, fim)
        print(f"Número aleatório gerado entre {inicio} e {fim}: {numero}")
    input("Pressione qualquer tecla para continuar...")

def operacoes_basicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print(f"\nResultados das operações entre {num1} e {num2}:")
    print(f"Adição: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")
    print(f"Multiplicação: {num1 * num2}")
    if num2 != 0:
        print(f"Divisão: {num1 / num2}")
    else:
        print("Divisão: impossível dividir por zero.")
    print(f"Potência: {num1 ** num2}")
    input("\nPressione qualquer tecla para continuar...")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nMenu de Operações")
        print("1. Raiz quadrada")
        print("2. Potência")
        print("3. Número aleatório")
        print("4. Sair")
        print("5. Operações básicas")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            raiz_quadrada()
        elif opcao == '2':
            potencia()
        elif opcao == '3':
            numero_aleatorio()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        elif opcao == '5':
            operacoes_basicas()
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para continuar...")

if __name__ == "__main__":
    main()
