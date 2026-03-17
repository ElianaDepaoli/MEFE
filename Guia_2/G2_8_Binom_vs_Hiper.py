import numpy as np
import matplotlib.pyplot as plt 
import math
import matplotlib.ticker as ticker
from scipy.stats import binom, poisson, hypergeom

N=5000#población total
n=500#Nuestra de la población total
pA=1/100#intención de voto al candidato A sobre la población total
perr=1/50#intención de voto al candidato A sobre la Nuestra de taNaño n
k=perr*n
print( k , "es la cantidad de individuos que representan el 2 % de la muestra ")
print("Integrar la pdf hasta", k , "para que la probabilidad de error sea menor al 2 % ")

#Aproximo la distribución de la muestra por una Poisson con esperanza mu = N*pA ~ n*pA
mu=n*pA
rv = poisson(mu)
p_error_pois=1-rv.cdf(k-1)
print("--------- Aproximo la distribución de la muestra por una Poisson con esperanza mu = N*pA ~ n*pA = ", mu ," -----------")
print("Probabilidad de obtener ", k, " o más votantes de A en la muestra: ", p_error_pois)

#Aproximo la distribución de la muestra por una binomial con n ensayos y probabilidad de éxito pA
print("--------- Aproximo la distribución de la muestra por una binomial con n ensayos y probabilidad de éxito pA -----------")
#Rango de X
rvB = binom(n, pA)
RxB = rvB.support()
p_error_bin = 1-rvB.cdf(k-1)
print("Probabilidad de obtener ", k, " o más votantes de A en la muestra: ", p_error_bin)
print("Rango de la variable aleatoria binomial = ", RxB)

#Cálculo exacto. La cantidad de éxitos tiene distribución hipergeométrica (Población total, cantidad de buenos, muestra)
rvh = hypergeom(N, pA*N, n)
#Rango de X
Rxh = rvh.support()
print("Rango de la variable aleatoria hipergeométrica	 = ", Rxh)
p_error_hyper_2=1-rvh.cdf(k-1)
print("---Cálculo exacto. H(", N, pA*N, n, ")")
print("Probabilidad de obtener ", k, " o más votantes de A en la  muestra:", p_error_hyper_2)

def diferencia_relativa(a,b):
	return (a-b)/a

diff_0 = 100*diferencia_relativa(p_error_hyper_2,p_error_bin )

print("diferencia relativa inicial = " , diff_0 , " % ")

diff_limite = 0.1 #el que fija la guía
aux = N
diff = diff_0

while math.fabs(diff) > diff_limite:
	aux = aux+5e4
	p_error_h=1-hypergeom.cdf(k-1, aux, pA*aux, n)
	diff = 100*diferencia_relativa(p_error_h, p_error_bin)
	print(aux, math.fabs(diff), p_error_h)

rvh_final = hypergeom(aux, pA*aux, n)

# Gráficos de las dos distribuciones -------------------------
#Array de numpy de números enteros entre los percentiles 0.01 y 0.99 de la binomial
x = np.arange(RxB[0], RxB[1]+1)#Array del rango de X
#x = np.arange(rv.ppf(0.01), rv.ppf(0.999))#Usando pasos por defecto (1)
#print("RXB = ", x, "Tipo de datos: ", type(x),)
#print("p_X(x) = ", rvB.pmf(x))
#print("Suma de p_X(x) sobre RX", round(sum(rv.pmf(x)),2))

#Grafico la función de probabilidad puntual o de masa de X 
fig, ax = plt.subplots(1, 1)
ax.stairs(rvB.pmf(x)[:20],x[:21], label= f'binom RX = {RxB}')
ax.stairs(rvh.pmf(x)[:20],x[:21], label= f'hipergeom RY = {Rxh}')
ax.stairs(rvh_final.pmf(x)[:20],x[:21], label= f'hipergeom N = {aux}')
#ax.plot(x, rv.pmf(x), 'bo', ms=8, label = f'p = {round(p, 2)}, n = {n}' )#, alpha=0.5
#ax.vlines(x, 0, rv.pmf(x), colors='b', lw=5, alpha=0.5)
ax.set_ylabel('p$_{X}$(x)')
ax.set_xlabel('x')
plt.legend()
plt.show()