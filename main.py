from modules.csv_reader import reader

#a)

googlelist = reader("google.csv")
nikelist = reader("nike.csv")

primertrimestre = []
for list in googlelist[0:90]:
    primertrimestre.append(float(list[-1]))

resistencia = max(primertrimestre)
soporte = min(primertrimestre)

caida_porciento = 100*(resistencia - soporte)/resistencia

print(caida_porciento)

#b) Si, se corresponde

#c)
anual = []

for lista in googlelist:
    anual.append(float(lista[-1]))

soporteanual = min(anual)

repunte = 100*(float(anual[-1])-soporteanual)/soporteanual

print(repunte)