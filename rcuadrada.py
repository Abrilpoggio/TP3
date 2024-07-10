def raiz_cuadrada_entera(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    return _raiz_cuadrada_entera_aux(n, 0, n)

def _raiz_cuadrada_entera_aux(n, inicio, fin):
    while inicio <= fin:
        medio = (inicio + fin) // 2
        cuadrado = medio * medio
        if cuadrado == n:
            return medio
        elif cuadrado < n:
            inicio = medio + 1
        else:
            fin = medio - 1
    return fin


numero = int(input("Introduce un número para calcular su raíz cuadrada entera: "))
resultado = raiz_cuadrada_entera(numero)
print(f"La raíz cuadrada entera de {numero} es {resultado}")
