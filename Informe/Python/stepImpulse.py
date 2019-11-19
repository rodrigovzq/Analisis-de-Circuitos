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
t, A = signal.lti.step(s1)
plt.figure()
plt.plot(t*1e3,A,'-g',linewidth = 1.8) # Grafica bode demodulo
plt.title('Respuesta al escalon')
plt.xlabel('Tiempo [ms]')
plt.ylabel('Amplitud [V]')
plt.legend(loc='upper left', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')


t, A = signal.lti.impulse(s1)
plt.figure()
plt.plot(t*1e3,A,'-g',linewidth = 1.8) # Grafica bode demodulo
plt.title('Respuesta al escalon')
plt.xlabel('Tiempo [ms]')
plt.ylabel('Amplitud [V]')
plt.legend(loc='upper left', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
plt.show()
