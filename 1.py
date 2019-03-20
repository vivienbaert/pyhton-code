import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy
plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")
plt.show()
