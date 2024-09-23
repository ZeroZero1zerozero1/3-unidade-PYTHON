numero = int(input("Digite um número:"))
fatorial = 1
contador = 1

while (contador <= numero):
    fatorial *= contador #fatorial = fatorial * contador
    contador += 1 # contador = contador + 1

print(f"o fatorial de {numero} é {fatorial}")