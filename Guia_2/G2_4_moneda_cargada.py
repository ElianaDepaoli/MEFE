import numpy as np
import matplotlib.pyplot as plt 
import math
import matplotlib.ticker as ticker

#Experimento: lanzar una moneda cargada hasta repetir el resultado del primer lanzamiento 
def lanzar_hasta_que_se_repita_primer_resultado(p):
	Y = []
	Y.append(rng.binomial(1,p)) #ensayos de Bernoulli con probabilidad de éxito p
	while True:
		a=rng.binomial(1,p)
		Y.append(a)
		if a==Y[0]:
			break

	return Y

#Inicialización del generador de números aleatorios
rng = np.random.default_rng()


p = 0.3 #probabilidad de éxito
#m =10 #cantidad de lanzamientos
#X = rng.binomial(1,p,m) #m ensayos de Bernoulli con probabilidad de éxito p
#print(X)

#Ejecuto una vez para probar. FUNCIONA.
#Y = lanzar_hasta_que_se_repita_primer_resultado(p)
#X = len(Y)
#print(Y, X)

#Muestreo la variable X: Nº total de lanzamientos hasta que se repite el primer resultado
m = 500
XX = []

for i in range(m):
	
	Y = lanzar_hasta_que_se_repita_primer_resultado(p)
	#print(Y)
	XX.append(len(Y))

cuentas, intervalos = np.histogram(XX, 10, density = False)
plt.stairs(cuentas,intervalos, label=f'p = {round(p, 2)}')
plt.yscale('linear')#linear #log
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_ylabel('p$_{X}$(x)')
ax.set_xlabel('x')
plt.title('X: Nº total de lanzamientos hasta que se repite el primer resultado')
plt.legend()
plt.show() 

