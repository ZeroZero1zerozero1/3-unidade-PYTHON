print("Olá, vamos ver qual será a sua média?")

nota1 = float(input("DIgite o valor da sua primeira nota  "))
nota2 = float(input("DIgite o valor da sua segunda nota "))
nota3 = float(input("DIgite o valor da sua terceira nota "))
nota4 = float(input("DIgite o valor da sua quarta nota "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Sua média é", media)

if (media >= 80):
    print("Aluno aprovado!!!")
elif(media >=60):
    print("Aluno reprovado!!!")
else:
        print("Aluno reprovado!!!")
