ano = int(input("Digite o ano: "))

if ano % 4 == 0 and ano % 1000 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
    print("O ano ", ano, "É bissexo")
else:
    print(f"O ano {ano} não é bissexto")