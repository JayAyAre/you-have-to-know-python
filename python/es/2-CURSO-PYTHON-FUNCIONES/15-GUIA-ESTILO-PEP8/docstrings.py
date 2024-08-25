# peps.python.org/pep-0008/

# Docstrings

# Mal
def f():
    pass

# Bien
def duplicar(numero1):
    """
    Returns the double of the number
    Args:
        numero1 (int or float): Int or float number to be doubled
    Returns:
        int or float: The doubled number
    """
    return numero1 * 2