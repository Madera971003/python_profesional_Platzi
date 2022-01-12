import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1 # yield es parecido a un return
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    # fibonacci = fibo_gen() # Instanciación del generador
    # for element in fibonacci:
    #     print(element)
    #     time.sleep(0.5)

    fibonacci2 = fibonacci_gen()
    for element in fibonacci2:
        print(element)
        time.sleep(0.5)