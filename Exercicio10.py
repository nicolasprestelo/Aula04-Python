numeroBase = int(input("Informe um número com 3 dígitos: "))

primeiroNumero = numeroBase // 100
resto = numeroBase % 100
segundoNumero = resto // 10
resto2 = resto % 10


inversao = str(primeiroNumero) + str(segundoNumero)

print(inversao)