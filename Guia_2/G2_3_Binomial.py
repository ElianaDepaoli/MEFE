import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
import math

# Funciones ----------------------------------------------------------------
def graficar_ncreciente_p_fijo(p, nn, columnas, filas, fig1, ax1):

	print("len(nn)", len(nn))
	print("filas", filas)
	axs = ax1.flatten()
	print(axs)

	for i, ax in enumerate(axs):
			if i ==len(nn):
				break

			rva = binom(nn[i], p)
			Rxa = rva.support()
			xa = np.arange(Rxa[0], Rxa[1]+1)
			ax.plot(xa, rva.pmf(xa), 'bo', ms=8, label = f'n = {nn[i]}')#
			ax.vlines(xa, 0, rva.pmf(xa), colors='b', lw=5, alpha=0.5)
			#ax1[i][j].set_title(f'p = {p}, n = {nn[l]}')
			ax.legend(loc=1)
	
	fig1.suptitle(f'p = {round(p,3)}')
	
	#plt.tight_layout()

#--------------------------------------------------
#v.a. X = "cantidad de éxitos en n intentos "
#Defino los parámetros de mi binomial
n = 20
p = 1/6.0

#objeto congelado
rv = binom(n, p)
#Rango de X
Rx = rv.support()
print("Rango de la variable aleatoria = ", Rx)
#Esperanza y varianza 
mean, var = rv.stats(moments='mv')
print('Esperanza = ', round(mean, 2), 'Varianza = ', round(var,2))

#Array de numpy de números enteros entre los percentiles 0.01 y 0.99 de la binomial
x = np.arange(Rx[0], Rx[1]+1)#Array del rango de X
#x = np.arange(rv.ppf(0.01), rv.ppf(0.999))#Usando pasos por defecto (1)
print("RX = ", x, "Tipo de datos: ", type(x),)
print("p_X(x) = ", rv.pmf(x))
print("Suma de p_X(x) sobre RX", round(sum(rv.pmf(x)),2))

#Grafico la función de probabilidad puntual o de masa de X 
fig, ax = plt.subplots(1, 1)
#ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.plot(x, rv.pmf(x), 'bo', ms=8, label = f'p = {round(p, 2)}, n = {n}' )#, alpha=0.5
ax.vlines(x, 0, rv.pmf(x), colors='b', lw=5, alpha=0.5)
ax.set_ylabel('p$_{X}$(x)')
ax.set_xlabel('x')
plt.legend()

#Varias distribuciones binomiales con n creciente y p fijo
nn = np.arange(59, 66)
columnas = 3
filas = math.ceil(len(nn)/columnas)
fig1, ax1 = plt.subplots(filas, columnas, figsize=(15,10))
graficar_ncreciente_p_fijo(1/6, nn, filas, columnas, fig1, ax1)
fig2, ax2 = plt.subplots(filas, columnas, figsize=(15,10))
graficar_ncreciente_p_fijo(0.5, np.arange(5, 17), filas, columnas, fig2, ax2)
plt.tight_layout()
plt.show()
#Fin -------------------------------------------------------------------


'''
l=0
for i in range(filas):
#	print(i)
	for j in range(columnas):
#		print(j)
		rva = binom(nn[l], p)
		Rxa = rva.support()
		xa = np.arange(Rxa[0], Rxa[1]+1)
		ax1[i][j].plot(xa, rva.pmf(xa), 'bo', ms=8, label = f'n = {nn[l]}')#
		ax1[i][j].vlines(xa, 0, rva.pmf(xa), colors='b', lw=5, alpha=0.5)
		l+=1
		print(l)
		#ax1[i][j].set_title(f'p = {p}, n = {nn[l]}')
		ax1[i][j].legend(loc=1)
		if l ==len(nn):
			break
'''