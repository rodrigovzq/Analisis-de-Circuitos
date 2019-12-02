import numpy as np
import csv
from scipy import signal
from matplotlib import pyplot as plt
import math
from scipy.special import exp10

## CUADRADOS MINIMOS
##Toma dos arreglos con los puntos de X y de Y respectivamente
##devuelve una tupla con la pendiente y la ordenada de la recta de regrecion
## necesita numpy como np
def LR(x,y):
  A = np.sum(((x-np.average(x))*(y-np.average(y))))/np.sum(np.power((x-np.average(x)),2))
  B = np.average(y)-A*np.average(x)
  return (A,B)

# Importo datos de medicion
medicion = open("/Users/rodrigovazquez/Library/Mobile Documents/3L68KQB4HG~com~readdle~CommonDocuments/Documents/ADC/TP2019/datos/medicionPasaAltos.csv","r")
datos = np.loadtxt(medicion,delimiter=',')
f = datos[:,0]
A = datos[:,1]

A1, B1 = LR(np.log10(f[5:18]),A[5:18])
A2, B2 = LR(np.log10(f[25:29]),A[25:29])
x1 = np.linspace(np.log10(f[1]),np.log10(f[16]),2*len(f[1:20]))
x2 = np.linspace(np.log10(f[16]),np.log10(f[29]),2*len(f[21:29]))
y1 = A1*x1+B1
y2 = A2*x2+B2

print("Pendiente asintota 1:"'\t')
print(A1)
print('\t')
print("Pendiente asintota 2:"'\t')
print(A2)




plt.semilogx(f[1:20],A[1:20],'.g',label = 'Curva medida') # Grafica bode de modulo
plt.semilogx(exp10(x1),y1,'-g',linewidth = 1.8,label = 'Ajuste')
plt.semilogx(f[21:29],A[21:29],'.r',linewidth = 1.8,label = 'Curva medida') # Grafica bode de modulo
plt.semilogx(exp10(x2),y2,'-r',linewidth = 1.8,label = 'Ajuste')
plt.title('Bode de modulo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.legend(loc='lower right', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
plt.show()
