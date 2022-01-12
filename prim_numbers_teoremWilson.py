def isPrime(number: int) -> bool: #Condigo con estructura tipo estatico
    """
    Function that applyes the Wilson's Theorem 
    to determine if a number is prime.
    """
    factorial = number -1
    for i in range(2, number-1):
        factorial *= i
    return (factorial + 1) % number == 0


def run():
    number: int = int(input("Ingrese un número: "))
    if isPrime(number):
        print("El número es primo")
    else:
        print("El número no es primo")


if __name__ == '__main__':
    run()