def calcularFatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcularFatorial(numero-1)

numero = 1
fatorial = calcularFatorial(numero)
print("O fatorial de",numero,"é",fatorial)
