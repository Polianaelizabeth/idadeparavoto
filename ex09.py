anoAtual = int(2023)
anoNascimento = int(input("digite o ano de nascimento"))

idade = anoAtual - anoNascimento

if idade >= 18:
    print("você tem ", idade, "anos. Deverá votar esse ano")
elif idade >= 16:
    print("você tem ", idade, "anos. Pode escolher se quer votar.")
else:
    print("você tem ", idade, "anos. Ainda nao tem idade para votar")
