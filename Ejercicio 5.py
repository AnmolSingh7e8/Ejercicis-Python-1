#Creem una matriu per el tauler d'escacs
tauler = [[" " for _ in range(9)] for _ in range(9)]

#Afegim les caselles del tauler
for fila in range(8):
    for columna in range(8):
        if (fila +columna) % 2 == 0:
            tauler[fila][columna] = "O"
        else:
            tauler[fila][columna] = "X"

#Afegim els numeros en a la dreta
for fila in range(8):
    tauler[fila][8] = str(8-fila)

#Afegim les lletres a la part de baix

lletres = ["A", "B", "C", "D", "E", "F", "G", "H"]


for col in range(8):
    tauler[8][col] = lletres[col]

#Casella buida a la cantonada inferior dreta
tauler[8][8] = " "

print("BENVINGUT AL TAULELL D'ESCACS:\n")

for fila in tauler:
    print(" ".join(fila))