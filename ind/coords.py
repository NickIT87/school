import matplotlib.pyplot as plt
#%matplotlib inline

plt.title("lesson1", color="black")
plt.xlabel("time min/hour", color="green")
plt.ylabel("speed km/h", color="green")
plt.xticks(color="red")
plt.yticks(color="red")
plt.axis(xmin=0,xmax=60,ymin=0,ymax=60)

plt.plot([0,30],
         [0,30])
plt.plot([30,50],
         [23,50])
plt.show()

# длина окружности 2*Pi*r