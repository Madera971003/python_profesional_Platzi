import time

def fibonacci_gen(max: int = 100000):
    a, b = 0, 1
    while a <= max:
        yield a
        a, b = b, a+b

if __name__ == '__main__':

    fibonacci = fibonacci_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)