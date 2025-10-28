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
    input ("Pressione Enter para continuar...")


def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} elevado a {expoente} é {resultado}")
    input ("Pressione qualquer telca para continuar...")

def numero_aleatorio():
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))
    if inicio > fim:
        print("O valor inicial deve ser menor ou igual ao valor final.")
    else:
        numero = random.randint(inicio, fim)
        print(f"numero aleatorio gerado entre {inicio} e {fim}: {numero}")
    input ("Pressione qualquer tecla para continuar...")
def main():
        while True:
            os.system("cls")
            print ("\n menu de operaçoes ")
            print("1.raiz quadrada")
            print("2.potencia")
            print("3.numero ramdomico")
            print("4.sair")

            opcao = input("Escolha uma opção:")
            if opcao == '1':
                raiz_quadrada()
            elif opcao == '2':
                potencia()
            elif opcao == '3':
                numero_aleatorio()
            elif opcao == '4':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
                
if __name__ == "__main__":
    main()