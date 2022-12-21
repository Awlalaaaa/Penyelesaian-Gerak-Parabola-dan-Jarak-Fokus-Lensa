Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Soal 1
... '''Rumus Fokus Lensa
...     1/f = (n-1)[1/R1 + 1/R2]
... '''
... 
... n  = 1.5     #Indeks Bias
... R1 = 20      #Jari-jari kelengkungan, satuan cm
... R2 = 18
... 
... F = (n-1)*((1/R1)+(1/R2))
... F = 1/F
... 
... print("-"*40)
... print("Jarak Fokus Lensa = ",F)
... 
... 
... #Soal 2
... import numpy as np
... import matplotlib.pyplot as plt
... 
... alpha = np.radians(45)
... g = 9.8
... v0 = 10
... 
... v0x = v0*np.cos(alpha)
... v0y = v0*np.sin(alpha)
... 
... X = ((v0**2)*np.sin(2*alpha))/(2*g)
... print("Jarak Horizontal Maksimum = ",X," m")
... Y = ((v0**2)*np.sin(2*alpha))/(2*g)
... print("Jarak  Maksimum = ",Y," m")
... T = (2*v0*np.sin(alpha))/g
... print("Waktu Mencapai Jarak Horizontal Maksimum = ",T," s")
... print("\n")
... 
... t = np.arange(0.0, T, 0.01)
... y = v0y*t - 0.5*g*t**2
... x = v0x*t
... 
... fig, ax = plt.subplots()
... ax.plot(x, y)
... ax.set(xlabel='x (m)', ylabel= 'y (m)', title='Grafik Gerak Parabola')
... ax.grid()
