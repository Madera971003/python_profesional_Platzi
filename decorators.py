from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre = "César"): # Este es un dato default, que se puede cambiar
    print("Hola " + nombre)

suma(5, 5)
random_func()
saludo("Abisai")


# Ejemplo con decorador que recibe un parametro, y otro una función
def with_custom_message(message):
    def with_message(function):
        print(f'{message}:')
        def wrapper(*args, **kwargs):
            c = function(*args, **kwargs)
            print(f"Este es el valor de c: {c}")
        return wrapper
    return with_message

@with_custom_message("Hello")
def multiply(a, b):
    c = a * b
    print(f"The result of {a} * {b} is {c}")
    return c

multiply(10, 2)