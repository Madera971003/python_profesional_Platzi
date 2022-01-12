import random
from datetime import datetime


# Primera solución
def remove_duplicates_Madera(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

# Una solución más rápida
def removeDuplicates(some_list):
    return list(set(some_list))

# Usando High order functions
Remove_Duplicates = lambda some_list: list(set(some_list))

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates_Madera(random_list))
    print(removeDuplicates(random_list))
    print(Remove_Duplicates(random_list))



# Usando verificación de tiempos de ejecución con dos formas

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print ('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time
def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    print('Lista sin duplicados: ', without_duplicates)

@execution_time
def remove_set(some_list):
    without_duplicates = set(some_list)
    print('Lista sin duplicados: ', without_duplicates)

def run2():
    random_list = [random.randint(1,10) for _ in range(10000000)]
    remove_duplicates(random_list)
    print('\nResultado con sets:')
    remove_set(random_list)

if __name__ == '__main__':
    run()
    run2()