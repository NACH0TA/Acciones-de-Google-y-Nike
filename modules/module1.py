from csv_reader import reader
import matplotlib.pyplot as plt
import math as m

googlelist = reader("google.csv")
nikelist = reader("nike.csv")

valoresgoogle = []
valoresnike = []

for lista in nikelist:
    fecha = lista[0]
    hora = lista[1]
    valor = float(lista[-1])
    valoresnike.append(valor)


for lista in googlelist:
    fecha = lista[0]
    hora = lista[1]
    valor = float(lista[-1])
    valoresgoogle.append(valor)

minimonike = min(valoresnike)
maximonike = max(valoresnike)
maxminnike = maximonike -minimonike

minimogoogle = min(valoresgoogle)
maximogoogle = max(valoresgoogle)
maxmingoogle = maximogoogle - minimogoogle

nuevovaloresnike = []
nuevovaloresgoogle = []

valoresnikeporciento = []
valoresgoogleporciento = []

for valor in valoresnike:
    valor1 = (valor-minimonike)/maxminnike
    nuevovaloresnike.append(valor1)
    valorporciento = 100*(valor - valoresnike[0])/valoresnike[0]
    valoresnikeporciento.append(valorporciento)
    

for valor in valoresgoogle:
    valor1 = (valor-minimogoogle)/maxmingoogle
    nuevovaloresgoogle.append(valor1)
    valorporciento = 100*(valor - valoresgoogle[0])/valoresgoogle[0]
    valoresgoogleporciento.append(valorporciento)

N= len(valoresnike) # cantidad de datos
f=1 # frecuencia Hz
tiempo = [i for i in range(N) ]
serie1 = nuevovaloresnike
serie2 = nuevovaloresgoogle
serie3 = valoresnikeporciento
serie4 = valoresgoogleporciento



# Gráfico PU

#first subplot

plt.subplot(1, 2, 1)    # 2 fila, 1 columnas, primer gráfico
plt.plot(tiempo,serie2, label="Google")
plt.title('Precios normalizados entre 0 y 1')
plt.grid()

plt.plot(tiempo,serie1, label="Nike")

plt.legend()

#second subplot

plt.subplot(1, 2, 2)
plt.plot(tiempo,serie4, label="Google")
plt.title('Tasa de variacion como porcentaje del precio inicial')
plt.grid()

plt.plot(tiempo,serie3, label="Nike")

plt.legend()
plt.show()