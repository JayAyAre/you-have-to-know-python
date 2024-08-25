print("".center(80,"-"))
print("TIENDA VIRTUAL".center(80, '-'))
print("".center(80, "-"), "\n")

option = 0
products = {"Camiseta": 10, "Pantalon": 20, "Jeans": 15, "Zapatos": 25, "Sombrero": 12}
cart = {}
while option != 3:
    print("\nMENU:")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Comprar productos y salir")
    while True:
        try:
            option = int(input("Elige una opción: "))
            if option not in [1, 2, 3]:
                print("Opción incorrecta")
        except ValueError:
            print("Opción incorrecta")
        else:
            break
    if option == 1:
        while True:
            try:
                [print(f"- Producto: {key} {products[key]}€") for key in products]
                name_new_item = input("Ingresa el nombre del producto a agregar: ")
                print("\nEscriba 'salir' para salir al menú principal")
                name_new_item = name_new_item.capitalize()
                if name_new_item in products:
                    print(f"Producto {name_new_item} agregado al carrito")
                    if cart.get(name_new_item, 0) == 0:
                        cart[name_new_item] = {
                            "name": name_new_item,
                            "price": products[name_new_item],
                            "quantity": 1
                        }
                    else:
                        cart[name_new_item]["quantity"] += 1
                    break
                elif name_new_item == "salir":
                    print("Operación cancelada")
                    break
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Producto no encontrado")
        print()
    elif option == 2:
        print("Carrito:\n")
        for key in cart:
            print(f"- Producto: {key} {cart[key]['price']}€, Cantidad: {cart[key]['quantity']}")
    elif option == 3:
        print("Comprar:")
        total = sum(cart[key]['price'] * cart[key]['quantity'] for key in cart)
        print(f"Total: {total}€")
        while True:
            try:
                amount_to_pay = int(input("Ingresa el monto a pagar: "))
                print()
            except ValueError:
                print("Ingresa un monto valido")
            else:
                break
        if amount_to_pay == total:
            print("Compra exitosa, no se requiere cambio")
            break
        elif amount_to_pay > total:
            print(f"Su cambio es: {amount_to_pay - total}€")
            break
        else:
            print("Compra fallida, monto insuficiente")
print("Gracias por comprar")
