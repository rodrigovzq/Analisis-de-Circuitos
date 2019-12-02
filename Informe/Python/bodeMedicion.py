import numpy as np
import csv
from scipy import signal
from matplotlib import pyplot as plt
import math


# Importo datos de medicion
medicion = open("/Users/rodrigovazquez/Library/Mobile Documents/3L68KQB4HG~com~readdle~CommonDocuments/Documents/ADC/TP2019/datos/medicionPasaAltos.csv","r")
datos = np.loadtxt(medicion,delimiter=',')
f = datos[:,0]
A = datos[:,1]

# Generador de transferencia en funcion de los coeficientes del numerador y denominador
numI = [1,0,0]
denI = [1,3510,1.004e7]
numR = [1,0,0]
denR = [1,(100000/33),9768868]

hz = np.logspace(6.2, 8)
rad_n = hz * 2 * np.pi / (1 / 5e-05)

s1 = signal.lti(numI,denI)
s2 = signal.lti(numR,denR)
wI, amplitudI, faseI = signal.bode(s1, w=rad_n)
wR, amplitudR, faseR = signal.bode(s2, w=rad_n)
wI = wI / 2 / np.pi
wR = wR / 2 / np.pi

# Graficos
plt.semilogx(wI,amplitudI,'-b',linewidth = 1.8,label = 'Curva ideal') # Grafica bode ideal
plt.semilogx(wR,amplitudR,'--r',linewidth = 1.8, label = 'Curva real')
plt.semilogx(f,A,'.g',linewidth = 1.8,label = 'Curva medida') # Grafica bode de modulo
plt.title('Bode de modulo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.legend(loc='lower right', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
plt.show()
