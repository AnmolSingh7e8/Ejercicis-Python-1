# Diccionari amb preus base (zona 1)
preus_base = {
    "1": ("Bitllet senzill", 2.20),
    "2": ("T-Casual", 10.20),
    "3": ("T-Mes", 54.00),
    "4": ("T-Trimestre", 145.30),
    "5": ("T-Jove", 105.00)
}

# Factors multiplicadors per zona
zones = {
    "1": 1.00,
    "2": 1.35,
    "3": 1.89
}

# Monedes i bitllets acceptats
diners_acceptats = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50,
                    1.00, 2.00, 5.00, 10.00, 20.00, 50.00]

continuar = "s"

while continuar.lower() == "s":
    # Selecció bitllet
    billet = input("Selecciona quin bitllet vols adquirir (Selecciona el número)?\n"
          "1. Bitllet senzill\n"
          "2. T-Casual\n"
          "3. T-Mes\n"
          "4. T-Trimestre\n"
          "5. T-Jove\n")

# Validació entrada bitllet
    if billet not in preus_base:
        print("Opció invàlida!\n")
        continuar = input("Vols intentar-ho de nou? (s/n): ")
        continue

    print("Has seleccionat:", preus_base[billet][0])

    # Selecció zona
    zona = input("Selecciona la zona del teu desplaçament (1, 2 o 3): ")
    if zona not in zones:
        print("Zona invàlida!\n")
        continuar = input("Vols intentar-ho de nou? (s/n): ")
        continue

    # Càlcul preu
    preu = round(preus_base[billet][1] * zones[zona], 2) # Redondeig a 2 decimals
    print(f"El preu del bitllet és: {preu:.2f} €")

    # Procés de pagament
    pagat = 0.0
    while pagat < preu:
        try:
            entrada = float(input(f"Introdueix diners (tens {pagat:.2f} €, falta {preu - pagat:.2f} €): "))
            if entrada in diners_acceptats:
                pagat += entrada
            else:
                print("Moneda o bitllet no acceptat.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número.")

    canvi = round(pagat - preu, 2)
    print(f"\nHas pagat {pagat:.2f} €. El teu canvi és {canvi:.2f} €.")
    print("Bitllet emès\n")

    # Preguntar si es vol comprar un altre bitllet
    continuar = input("Vols comprar un altre bitllet? (s/n): ")

print("Gràcies per utilitzar la màquina!")




