Banco_Saldo = 600
while True:
 Retiro = (int(input("Bienvenido a Banco America, cuanto desea retirar? ")))
 if Retiro > Banco_Saldo:
    print (f"Lo sentimos, no hay saldo suficiente. Necesita {Retiro - Banco_Saldo} ")
    input(" Presione Enter para hacer otro retiro")
 else:
    print (f" Retirto con exito, tu saldo actual es de {Banco_Saldo - Retiro} ")
    Banco_Saldo = Banco_Saldo - Retiro
    print (" Escriba 'N' para hacer otro retiro / Esriba 'S' para terminar.")
    interaccion = input(" Type here: ")
    if interaccion == "N":
        continue
    elif interaccion == "S":
        print ("Gracias por usar Banco America, vuelva pronto")
        break
    else:
        print ("Opcion no valida, deseas salir 'S' o reintentar 'R'?")
        interaccion2 = (input("Type here: "))
        if interaccion2 == "S":
            print (" Gracias por usar Banco America, Vuelva pronto")
            break
        elif interaccion2 == "R":
            continue
        
