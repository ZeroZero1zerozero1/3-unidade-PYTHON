print("Programa para cálculo de IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
IMC = peso / (altura ** 2)

print(f"Seu IMC é {IMC:.2f}.")
print("Classificação do IMC:")
if IMC < 18.5:
    print("Abaixo do peso normal.")
elif 18.5 <= IMC < 25:
    print ("Peso normal.")
elif 25 <= IMC < 30:
    print("Sobrepeso.")
elif 30 <= IMC < 35:
    print("Obesidade grau I")
elif 35 <= IMC < 40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")