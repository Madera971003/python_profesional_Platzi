def make_division_by(n: int):
    """ This closures returns a function that returns the dision
        of an x number by n
    """
    # Desventaja del lambda, no se puede hacer verificación de forma estática
    #return lambda x: x/n # Esta línea es una buena solución a lo de abajo

    def divisor(x: int):
        assert type(x) == int, "Solo puedes utilizar números enteros"
        return x/n
    return divisor

division_by_3 = make_division_by(3)
print(division_by_3(18)) # The expected output is 6

division_by_5 = make_division_by(5)
print(division_by_5(100)) # The exécted output is 20

division_by_18 = make_division_by(18)
print(division_by_18(54)) # The expected output is 3