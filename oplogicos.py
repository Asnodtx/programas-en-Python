# con el operador and se deben de cumplir las dos condiciones 
# con el operador or se debe cumplir una o dos condiciones 
# con el operador not el verdadero se converte en falso 

temperatura = int(input("Cual es la temperatura afuera? "))

# if temperatura >= 0 and temperatura <= 30:
#     print("La temperatura esta bien")
# elif temperatura < 0 or temperatura > 30:
#     print("La temperatura esta mal")

if not(temperatura >= 0 and temperatura <= 30):
    print("La temperatura esta bien")
elif not(temperatura < 0 or temperatura > 30):
    print("La temperatura esta mal")