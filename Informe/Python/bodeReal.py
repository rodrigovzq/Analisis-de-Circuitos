import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import math

#Generador de transferencia en funcion de los coeficientes del numerador y denominador
numI = [1,0,0]
denI = [1,3510,1.004e7]
numR = [1,0,0]
denR = [1,(100000/33),9768868]

hz = np.logspace(0, 11)
rad_n = hz * 2 * np.pi / (1 / 5e-05)

s1 = signal.lti(numI,denI)
s2 = signal.lti(numR,denR)
wI, amplitudI, faseI = signal.bode(s1, w=rad_n)
wR, amplitudR, faseR = signal.bode(s2, w=rad_n)
wI = wI / 2 / np.pi
wR = wR / 2 / np.pi

plt.semilogx(wI,amplitudI,'-b',linewidth = 1.8,label = 'Curva ideal') # Grafica bode demodulo
plt.semilogx(wR,amplitudR,'--r',linewidth = 1.8, label = 'Curva real')
plt.title('Bode de modulo')
plt.xlabel('Frecuencia [Hz] ')
plt.ylabel('Amplitud [dB]')
plt.legend(loc='upper left', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
#plt.savefig('/BodeModulo.png',dpi=300)

plt.figure()
plt.semilogx(wI,faseI,'-b',linewidth = 1.8, label = 'Curva ideal') #Grafica bode de fase
plt.semilogx(wR,faseR,'--r',linewidth = 1.8, label = 'Curva real')
plt.title('Bode de fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [grados]')
plt.legend(loc='upper right', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
plt.show()
