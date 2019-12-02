import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import math

#Generador de transferencia en funcion de los coeficientes del numerador y denominador
num = [1,0,0]
den = [1,3510,1.004e7]

hz = np.logspace(0, 11)
rad_n = hz * 2 * np.pi / (1 / 5e-05)

s1=signal.lti(num,den)
w, amplitud, fase = signal.bode(s1, w=rad_n)
w = w / 2 / np.pi

plt.semilogx(w,amplitud,'-b',linewidth = 1.8) # Grafica bode demodulo
plt.title('Bode de modulo')
plt.xlabel('Frecuencia [Hz] ')
plt.ylabel('Amplitud [dB]')
plt.legend(loc='upper left', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
#plt.savefig('/BodeModulo.png',dpi=300)

plt.figure()
plt.semilogx(w,fase,'-r',linewidth = 1.8) #Grafica bode de fase
plt.title('Bode de fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [grados]')
plt.legend(loc='upper left', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
plt.show()
#plt.savefig('.. /Graficos/BodeFase.png',dpi=300)
