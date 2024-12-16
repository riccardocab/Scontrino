#16/12/24

#nome prodotto
#quantità desiderata
#prezzo

item = input("Che cosa vuoi comprare? ")
price = input("Quanto costa? ")
qnt = input("Quanti ne compri? ")

#metodo1 CALCOLARE IL RISULTATO E METTERLO IN UNA VARIABILE
tot = int(qnt) * float(price)
print(f"Dovrà pagare {str(float(tot))} euro per le sue {int(qnt)} {item}")
print("Per comprare " + qnt + " di " + item + " devi pagare " +str(tot))





