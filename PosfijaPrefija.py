def evaluar_expresion(expresion, tipo):
    pila = []
    tokens = expresion.split()[::-1] if tipo == 'prefija' else expresion.split()
    for token in tokens:
        if token.isdigit():
            pila.append(int(token))
        else:
            b, a = pila.pop(), pila.pop()
            pila.append(eval(f'{a} {token} {b}'))  
    return pila.pop()

def menu():
    print("\n=== Menú de Operaciones Aritméticas ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Selecciona una operación (1-5): ")
    if opcion == '1':
        operador = '+'
    elif opcion == '2':
        operador = '-'
    elif opcion == '3':
        operador = '*'
    elif opcion == '4':
        operador = '/'
    elif opcion == '5':
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Intenta de nuevo.")
        return menu()
    return operador

def crear_expresion(operador, tipo):
    a = input("Introduce el primer operando: ")
    b = input("Introduce el segundo operando: ")
    return f"{operador} {a} {b}" if tipo == 'prefija' else f"{a} {b} {operador}"

def main():
    while True:
        operador = menu()
        if operador == 'salir':
            print("Saliendo del programa...")
            break
        elif not operador:
            print("Opción inválida. Intenta de nuevo.")
            continue
        tipo = input("Elige el tipo de notación (postfija/prefija): ").strip().lower()
        if tipo not in ['postfija', 'prefija']:
            print("Tipo de notación no válido. Intenta de nuevo.")
            continue

        expresion = crear_expresion(operador, tipo)
        resultado = evaluar_expresion(expresion, tipo)
        print(f"Resultado de la operación ({expresion}): {resultado}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()