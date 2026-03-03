"""
Módulo que contiene la función es_primo.
"""

def es_primo(numero):
    """
    Determina si un número es primo.

    Un número primo es un número mayor que 1 que solo es divisible
    entre 1 y sí mismo.

    Parámetros:
        numero (int): Número entero a evaluar.

    Retorna:
        bool: True si es primo, False si no lo es.

    Lanza:
        TypeError: Si el argumento no es un entero.
        ValueError: Si el número es menor que 2.
    """

    # Validar tipo
    if not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")

    # Validar que sea mayor o igual a 2
    if numero < 2:
        raise ValueError("El número debe ser mayor o igual a 2.")

    # Verificar divisibilidad
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True