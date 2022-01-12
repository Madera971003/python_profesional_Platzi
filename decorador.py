# Primer ejemplo de decorador
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original")
        func()
    return envoltura

@decorador
def saludo():
    print("¡Hola!")

saludo()

# Segundo ejemplo de decorador
def mayusculas(func):
    def envoltura(texto: str):
        assert type(texto) == str, "Debes ingresar una cadena"
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje("César"))