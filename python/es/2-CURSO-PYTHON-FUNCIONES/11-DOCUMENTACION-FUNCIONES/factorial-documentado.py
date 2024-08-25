def factorial(n):
    """
    Calcula el factorial de un numero entero positivo.

    Args:
        n (int): Numero entero positivo

    Returns:
        n! (int): El factorial del n

    Raises:
        RecursionError: Si n es negativo.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



print(factorial(5))