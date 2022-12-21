import matplotlib.pyplot as plt
import numpy as np

# створення датасету у вигляді списку координат:
x = np.arange(0, 4*np.pi-1, 0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

# друк відповідних графіків
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])      
plt.show()