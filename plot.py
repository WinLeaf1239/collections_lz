import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,30,100) #область определения и мн-во точек
y = x **2 + x*2 +8 #Функция
plt.plot(x, y) #График
plt.show() #Вывод