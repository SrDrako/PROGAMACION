import os

lotes_disponibles = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

clientes = []

detalles_lotes = {
    1: {"tamaño": "200 m²", "precio": "$100,000"},
    2: {"tamaño": "150 m²", "precio": "$80,000"},
    3: {"tamaño": "180 m²", "precio": "$90,000"},
    4: {"tamaño": "250 m²", "precio": "$120,000"},
    5: {"tamaño": "170 m²", "precio": "$85,000"},
    6: {"tamaño": "190 m²", "precio": "$95,000"},
    7: {"tamaño": "220 m²", "precio": "$110,000"},
    8: {"tamaño": "200 m²", "precio": "$100,000"},
    9: {"tamaño": "150 m²", "precio": "$80,000"},
    10: {"tamaño": "180 m²", "precio": "$90,000"},
    11: {"tamaño": "200 m²", "precio": "$100,000"},
    12: {"tamaño": "150 m²", "precio": "$80,000"},
    13: {"tamaño": "180 m²", "precio": "$90,000"},
    14: {"tamaño": "250 m²", "precio": "$120,000"},
    15: {"tamaño": "170 m²", "precio": "$85,000"},
    16: {"tamaño": "190 m²", "precio": "$95,000"},
    17: {"tamaño": "220 m²", "precio": "$110,000"},
    18: {"tamaño": "200 m²", "precio": "$100,000"},
    19: {"tamaño": "150 m²", "precio": "$80,000"},
    20: {"tamaño": "180 m²", "precio": "$90,000"},

}

def limpiar_pantalla():
    if os.name == "nt":
        
        os.system("cls")

def mostrar_disponibilidad():

    print('              ----------LISTA GENERAL DE LOTES ---------- ')
    print("1:  tamaño: 200 m², precio: $100,000, coordenadas: (fila: 0, columna: 0)\n"
        "2:  tamaño: 150 m², precio: $80,000,  coordenadas: (fila: 0, columna: 1)\n"
        "3:  tamaño: 180 m², precio: $90,000,  coordenadas: (fila: 0, columna: 2)\n"
        "4:  tamaño: 250 m², precio: $120,000, coordenadas: (fila: 0, columna: 3)\n"
        "5:  tamaño: 170 m², precio: $85,000,  coordenadas: (fila: 0, columna: 4)\n"
        "6:  tamaño: 190 m², precio: $95,000,  coordenadas: (fila: 1, columna: 0)\n"
        "7:  tamaño: 220 m², precio: $110,000, coordenadas: (fila: 1, columna: 1)\n"
        "8:  tamaño: 200 m², precio: $100,000, coordenadas: (fila: 1, columna: 2)\n"
        "9:  tamaño: 150 m², precio: $80,000,  coordenadas: (fila: 1, columna: 3)\n"
        "10: tamaño: 180 m², precio: $90,000,  coordenadas: (fila: 1, columna: 4)\n"
        "11: tamaño: 200 m², precio: $100,000, coordenadas: (fila: 2, columna: 0)\n"
        "12: tamaño: 150 m², precio: $80,000,  coordenadas: (fila: 2, columna: 1)\n"
        "13: tamaño: 180 m², precio: $90,000,  coordenadas: (fila: 2, columna: 2)\n"
        "14: tamaño: 250 m², precio: $120,000, coordenadas: (fila: 2, columna: 3)\n"
        "15: tamaño: 170 m², precio: $85,000,  coordenadas: (fila: 2, columna: 4)\n"
        "16: tamaño: 190 m², precio: $95,000,  coordenadas: (fila: 3, columna: 0)\n"
        "17: tamaño: 220 m², precio: $110,000, coordenadas: (fila: 3, columna: 1)\n"
        "18: tamaño: 200 m², precio: $100,000, coordenadas: (fila: 3, columna: 2)\n"
        "19: tamaño: 150 m², precio: $80,000,  coordenadas: (fila: 3, columna: 3)\n"
        "20: tamaño: 180 m², precio: $90,000,  coordenadas: (fila: 3, columna: 4)\n")

    print("              ----------DISPONIBILIDAD DE LOTES ----------")
    for fila in lotes_disponibles:
        for lote in fila:
            if lote == 0:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print()
    

def seleccionar_lote():
    limpiar_pantalla()
    mostrar_disponibilidad()
    print()
    fila = int(input("Ingrese el número de fila del lote: "))
    columna = int(input("Ingrese el número de columna del lote: "))

    if fila < 0 or fila >= len(lotes_disponibles) or columna < 0 or columna >= len(lotes_disponibles[0]):
        print("Coordenadas inválidas. Por favor, ingrese coordenadas válidas.")
        return

    if lotes_disponibles[fila][columna] == 0:
        rut = int(input("Ingrese su RUT: "))
        nombre = input("Ingrese su nombre completo: ")
        telefono = input("Ingrese su teléfono: ")
        email = input("Ingrese su email: ")

        cliente = {
            "rut": rut,
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "fila": fila,
            "columna": columna
        }

        clientes.append(cliente)
        lotes_disponibles[fila][columna] = 1

        numero_lote = obtener_numero_lote(fila, columna)
        cliente["numero_lote"] = numero_lote
        print("Lote seleccionado con éxito.")
    else:
        print("El lote seleccionado no está disponible. Por favor, elija otro lote.")

def obtener_numero_lote(fila, columna):
    numero_lote = columna + fila * len(lotes_disponibles[0]) + 1
    return numero_lote

def mostrar_detalles_lote():
    rut = int(input("Ingrese su RUT: "))
    for cliente in clientes:
        if cliente["rut"] == rut:
            fila = cliente["fila"]
            columna = cliente["columna"]
            if fila < 0 or fila >= len(lotes_disponibles) or columna < 0 or columna >= len(lotes_disponibles[0]):
                print("Coordenadas del lote inválidas.")
                return

            numero_lote = obtener_numero_lote(fila, columna)
            detalles = detalles_lotes.get(numero_lote)
            if detalles:
                print("Detalles del lote:")
                print("Número de lote:", numero_lote)
                print("Tamaño:", detalles["tamaño"])
                print("Precio:", detalles["precio"])
            else:
                print("No se encontraron detalles para el cliente con RUT:", rut)
            return
    print("No se encontró ningún cliente con RUT:", rut)

def mostrar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print("RUT:", cliente["rut"])
        print("Nombre:", cliente["nombre"])
        print("Teléfono:", cliente["telefono"])
        print("Email:", cliente["email"])
        print("Número de lote:", cliente["numero_lote"])
        print("--------------------")

def ejecutar_programa():
    while True:
        limpiar_pantalla()
        print("Bienvenido a LotesDuoc")
        print("1. Mostrar disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Mostrar detalles de un lote")
        print("4. Ver Clientes")
        print("5. Salir")
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            limpiar_pantalla()
            mostrar_disponibilidad()
            input("Presione Enter para continuar...")
        elif opcion == "2":
            seleccionar_lote()
            input("Presione Enter para continuar...")
        elif opcion == "3":
            limpiar_pantalla()
            mostrar_detalles_lote()
            input("Presione Enter para continuar...")
        elif opcion == "4":
            limpiar_pantalla()
            mostrar_clientes()
            input("Presione Enter para continuar...")
        elif opcion == "5":
            print("Gracias por utilizar el Sistema de Lotes Residenciales. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

ejecutar_programa()
