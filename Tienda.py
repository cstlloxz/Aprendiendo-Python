Balon = 25
Cleats = 70
Espinilleras = 5
Dinero = 105
print (f"Bienvenido a la tienda Sports. Su saldo es de {Dinero} que desea comprar?")
print ("1. Balon $25")
print ("2. Cleats $70")
print ("3. Espinilleras $5")
while True:
    Compra = input("ingresa el producto que deseas comprar/escriba (Salir) para salir/ Ingresa (Productos) para ver productos: ")
    if Compra == "Salir":
        print(" Hasta luego")
        break
    elif Compra == "Productos":
        print ("1. Balon $25")
        print ("2. Cleats $70")
        print ("3. Espinilleras $5")
    elif Compra == "Balon":
        if Dinero < Balon:
            print (" Lo sentimos, tu saldo es insuficiente!")
            break
        else:
            Dinero = Dinero - Balon
        print (f" Compra exitosa, tu saldo es de {Dinero}")
    elif Compra == "Cleats":
        if Dinero < Cleats:
            print (" Lo sentimos, tu saldo es insuficiente!")
            break
        else:
            Dinero = Dinero - Cleats
        print (f" Compra exitosa, tu saldo es de {Dinero}")
    elif Compra == "Espinilleras":
        if Dinero < Espinilleras:
            print (" Lo sentimos, tu saldo es insuficiente!")
            break
        else:
            Dinero = Dinero - Espinilleras
        print (f" Compra exitosa, tu saldo es de {Dinero}")