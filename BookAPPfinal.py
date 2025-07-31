from datetime import datetime

friends = {}
books = {}
bookings = {}

def create_friend():
    friend = []
    id_friend = int(input("Id Amigo: "))
    name_friend = input("Nombre amigo: ")
    friend.append(name_friend)
    phone = input("Teléfono: ")
    friend.append(phone)
    friends[id_friend] = friend
    print("Amigo registrado exitosamente.\n")

def create_book():
    book = []
    id_book = int(input("Id libro: "))
    book_name = input("Nombre del libro: ")
    book.append(book_name)
    author = input("Autor: ")
    book.append(author)
    book.append(True)  
    books[id_book] = book
    print("Libro registrado exitosamente.\n")

def book_loan():
    loan = []
    id_loan = int(input("ID del préstamo: "))

    id_friend = int(input("ID del amigo: "))
    if id_friend not in friends:
        print("Amigo no encontrado.\n")
        return

    id_book = int(input("ID del libro: "))
    if id_book not in books:
        print("Libro no encontrado.\n")
        return

    if books[id_book][2] == False:
        print("Este libro ya está prestado.\n")
        return

    loan.append(friends[id_friend][0])  
    loan.append(books[id_book][0])      

    fecha_prestamo = input("Fecha del préstamo (dd/mm/aaaa): ")
    loan.append(fecha_prestamo)

    fecha_devolucion = input("Fecha estimada de devolución (dd/mm/aaaa): ")
    loan.append(fecha_devolucion)

    bookings[id_loan] = loan
    books[id_book][2] = False  
    print("Préstamo registrado exitosamente.\n")

def show_friends():
    print("\n--- Lista de Amigos ---")
    for id, data in friends.items():
        print(f"ID: {id} | Nombre: {data[0]} | Teléfono: {data[1]}")
    print()

def show_books():
    print("\n--- Lista de Libros ---")
    for id, data in books.items():
        estado = "Disponible" if data[2] else "Prestado"
        print(f"ID: {id} | Título: {data[0]} | Autor: {data[1]} | Estado: {estado}")
    print()

def show_bookings():
    print("\n--- Lista de Préstamos ---")
    for id, data in bookings.items():
        print(f"ID Préstamo: {id} | Amigo: {data[0]} | Libro: {data[1]} | Desde: {data[2]} hasta {data[3]}")
    print()

def verificar_devoluciones():
    hoy = datetime.now().strftime("%d/%m/%Y")
    print(f"\nFecha de hoy: {hoy}")
    print("Mensajitos de recordatorio:")
    encontrado = False
    for id, data in bookings.items():
        fecha_devolucion = data[3]
        if fecha_devolucion == hoy:
            print(f"Hoy se debe devolver el libro '{data[1]}' que prestó {data[0]}.")
            encontrado = True
    if not encontrado:
        print("No hay devoluciones programadas para hoy.")
    print()

def menu():
    while True:
        print("==== MENÚ PRINCIPAL ====")
        print("1. Registrar amigo")
        print("2. Registrar libro")
        print("3. Registrar préstamo")
        print("4. Ver amigos")
        print("5. Ver libros")
        print("6. Ver préstamos")
        print("7. Ver recordatorios de devolución")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            create_friend()
        elif opcion == "2":
            create_book()
        elif opcion == "3":
            book_loan()
        elif opcion == "4":
            show_friends()
        elif opcion == "5":
            show_books()
        elif opcion == "6":
            show_bookings()
        elif opcion == "7":
            verificar_devoluciones()
        elif opcion == "8":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

menu()
