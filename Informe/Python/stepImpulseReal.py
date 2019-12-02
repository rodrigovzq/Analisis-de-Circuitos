import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import math

#Generador de transferencia en funcion de los coeficientes del numerador y denominador
num = [1,0,0]
den = [1,3510,1.004e7]
numR = [1,0,0]
denR = [1,(100000/33),9768868]

hz = np.logspace(0, 11)
rad_n = hz * 2 * np.pi / (1 / 5e-05)

s1=signal.lti(num,den)
s2 = signal.lti(numR,denR)
t, A = signal.lti.step(s1)
tR, AR = signal.lti.step(s2)

plt.figure()
plt.plot(t*1e3,A,'-b',linewidth = 1.8,label = 'Curva ideal')
plt.plot(tR*1e3,AR,'--r',linewidth = 1.8, label = 'Curva real') # Grafica bode demodulo
plt.title('Respuesta al escalon')
plt.xlabel('Tiempo [ms]')
plt.ylabel('Amplitud [V]')
plt.legend(loc='upper right', fontsize = 'large')
plt.grid(which = 'major', color = 'gray', linestyle = '--')
plt.minorticks_on()
plt.grid(which = 'minor', color = '#bababa', linestyle = ':')
plt.show()
