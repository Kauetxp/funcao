def palindromo(texto):
    texto = texto.lower().replace(" ","")
    return texto == texto[::-1]
    
texto =  "subi no onibus"
if palindromo(texto):
    print(texto, "é um palíndromo")
else:
    print(texto, "não é um palíndromo")
