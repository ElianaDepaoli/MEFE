import numpy as np
import matplotlib.pyplot as plt 
import math
import matplotlib.ticker as ticker
from scipy.stats import binom, poisson, hypergeom

#probabilidad de gol por ensayo (patear al arco)
pg=18.2/100

def proba_al_menos_2(pg,n):
	return 1-np.power(1-pg,n)-n*np.power(pg,1)*np.power(1-pg,n-1)

print(proba_al_menos_2(pg,20))

print("Esperanza = ", 20*.182)