def prime_number(number: int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
        return True
    return False

def run():
    n: int = int(input('Escribe un número: '))
    if prime_number(n):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == '__main__':
    run()