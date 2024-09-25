# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
Soma = 0
contagem = 0

while True:
    número = float(input("Digite um número (-1 para sair): "))
    
    if número == -1:
        break
    
    Soma = Soma + número
    contagem = contagem + 1

if contagem > 0:
    Média = Soma / contagem
    print(f"A média dos números digitados é: {Média}")

    
