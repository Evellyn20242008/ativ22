# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.

def somar_numeros():
    soma = 0
    
    while True:
        numero = float(input("Digite um número (ou 0 para sair): "))
        
        if numero == 0:
            break
        
        soma += numero
    
    print(f"A soma total é: {soma}")

somar_numeros()

