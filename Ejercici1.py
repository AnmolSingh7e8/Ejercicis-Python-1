litresAigua = float(input("Introdueix els litres d'aigua consumits: "))
cuota = 6

# Càlcul de la quota segons el consum
if 50 < litresAigua < 200:
    cuota += litresAigua * 0.1
elif litresAigua > 200:
    cuota += litresAigua * 0.1
else:
    print("La quota no canvia")

print(f"La quota final és: {cuota} €")
