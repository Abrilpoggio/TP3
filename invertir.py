def invertir_secuencia(secuencia):
    return secuencia[::-1]

frase = input("Introduce una frase para invertir: ")
frase_invertida = invertir_secuencia(frase)
print(f"La frase invertida es: {frase_invertida}")

