# Візуалізація задачі "Кидок тіла під кутом до горизонту в безповітряному просторі"
# created by NickIT87

import matplotlib.patches as mpatches   # імпорт mpl для відображення "легенди"
import matplotlib.pyplot as plt         # программний об'єкт для відображення графіку
import numpy as np                      # бібліотека для роботы з двовимірними масивами
from scipy.constants import g           # гравітаійна константа
from math import pow

# базові налаштування координатної сітки
fig = plt.figure()
axes = plt.axes(projection='3d')

# зазначення міток та кольорів координатної сітки
axes.set_xlabel("X [abscissus] - dist. m.", color='black')
axes.set_ylabel("Y [ordinatus] - n/a", color='black')
axes.set_zlabel("Z [applicata] - alt. m.", color='black')
axes.tick_params(axis='x', colors='darkred')
axes.tick_params(axis='y', colors='darkgreen')
axes.tick_params(axis='z', colors='darkblue')

# налаштування шагу координатної сітки
axes.set_xlim([0,60000])    # X
axes.set_ylim([-5,5])       # Y
axes.set_zlim([0,30000])    # Z

# Заголовок графіка
axes.set_title(
    '''Рух важкої матеріальної точки, кинутої під кутом до горизонту.\n
     (в однорідному полі тяжіння та безповітряному просторі) \n''', 
    color='black'
)

# функція розрахунку параболи
def draw_trajectory(V0:int, alpha:int, t_color:str, t_label:str, step:int=0, p_safe=False):
    # Час польоту
    t = 2 * V0 / g * np.sin(np.deg2rad(alpha))
    # Максимальний під'єм
    H = pow(V0, 2)/(2*g) * pow(np.sin(np.deg2rad(alpha)), 2)
    # горизонтальна відстань, X1 = 0
    X2 = pow(V0, 2)*np.sin(np.deg2rad(alpha * 2))/g

    # рівняння руху
    x=np.array(
        [V0*dt*np.cos(np.deg2rad(alpha)) for dt in range(int(t))]
    )
    y=np.array(
        [step for dt in range(int(t))]  #Вісь y = 0 (рух повітря не враховуємо)
    )
    z=np.array(
        # загальне рівняння руху з диференціюванням за часом
        # [V0*dt*np.sin(np.deg2rad(alpha))-0.5*g*pow(dt, 2) for dt in range(int(t))]
        
        # дифференціювання за віссю Х (виключено параметр t)
        [
            dx*np.tan(np.deg2rad(alpha))-g*pow(dx,2)/(2*pow(V0,2)*pow(np.cos(np.deg2rad(alpha)),2))
            for dx in x
        ]
    )
    # парабола безпеки
    z_safety = np.array(
        [
            pow(V0,2)/(2*g) - g/(2*pow(V0,2))*pow(dx, 2)
            for dx in x
        ]
    )
    # відображення параболи
    axes.plot3D(x,y,z, t_color)
    # відображення параболи безпеки, якщо аргумент p_safe=True
    if p_safe:
        axes.plot3D(x,y,z_safety, 'green')
    # максимальна точка під'єму
    axes.scatter3D(X2/2, step, H, marker='x', c=t_color)
    # максимальна відстань
    axes.scatter3D(X2, step, 0, marker='*', c=t_color)
    # текст опису ТТВ, "легенда"
    return mpatches.Patch(
        color=t_color, 
        label=t_label + ' - V0:{0}m/s alpha:{1}deg H:{2:.2f}m t:{3:.2f}s S:{4:.2f}m'.format(
            V0, alpha, H, t, X2
        )
    )

# початкові швидкості снарядів для полкової гаубиці Д30:
# ОФЗ 690 м/с  КМЛ 740 м/с

p1 = draw_trajectory(
    V0=690, alpha=45, t_color='blue', t_label='HIGH-EXPLOSIVE projectile', step=-4, p_safe=True
)
p2 = draw_trajectory(V0=740, alpha=45, t_color='red', t_label='HEAT projectile', p_safe=True)
p3 = draw_trajectory(V0=690, alpha=30, t_color='magenta', t_label='FlatTrajectory', step = 4)
p4 = draw_trajectory(V0=690, alpha=60, t_color='magenta', t_label='HingedTrajectory', step = 4)

# відображення легенды та графіку
safety_parabola = mpatches.Patch(color='green', label='Парабола безпеки')
axes.legend(handles=[p1, p2, p3, p4, safety_parabola], loc='upper left')
plt.show()