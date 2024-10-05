import time
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return None

    def mostrar(self):
        return self.elementos

# Función recursiva para resolver el problema de las Torres
def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        # Movimiento directo cuando solo queda un disco
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover el disco {disco} de {origen.nombre} a {destino.nombre}")
        time.sleep(1)
    else:
        # Mover n-1 discos del origen al auxiliar usando el destino como auxiliar
        torres_de_hanoi(n-1, origen, auxiliar, destino)
        # Mover el disco restante del origen al destino
        torres_de_hanoi(1, origen, destino, auxiliar)
        # Mover los n-1 discos del auxiliar al destino usando el origen como auxiliar
        torres_de_hanoi(n-1, auxiliar, destino, origen)

# Función para inicializar el juego de las Torres de Hanoi con 3 discos
def iniciar_juego():
    # Se crean las tres torres
    torre1 = Pila()
    torre2 = Pila()
    torre3 = Pila()

    # Se le asignan nombres a las torres para referencia
    torre1.nombre = "Torre 1"
    torre2.nombre = "Torre 2"
    torre3.nombre = "Torre 3"

    # Apilamos los discos en la primera torre (del más grande al más pequeño)
    torre1.apilar(3)
    torre1.apilar(2)
    torre1.apilar(1)

    # Mostramos el estado inicial
    print("Estado inicial:")
    print(f"Torre 1: {torre1.mostrar()}")
    print(f"Torre 2: {torre2.mostrar()}")
    print(f"Torre 3: {torre3.mostrar()}")
    time.sleep(1)

    # Llamamos a la función recursiva para resolver el problema
    print("\nResolviendo...\n")
    time.sleep(1)
    torres_de_hanoi(3, torre1, torre3, torre2)

    # Mostramos el estado final
    print("\nResuelto:")
    print(f"Torre 1: {torre1.mostrar()}")
    print(f"Torre 2: {torre2.mostrar()}")
    print(f"Torre 3: {torre3.mostrar()}")
    time.sleep(1)
    print("Fin del programa :D\n")

# Para ejecutar el juego
iniciar_juego()
