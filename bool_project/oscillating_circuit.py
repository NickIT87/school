import lcapy as lc
from lcapy import Vstep, R, L, C, t
from matplotlib.pyplot import savefig
from numpy import linspace

L = 1 # індуктивність в Гн
C = 1e-6 # ємність в Ф

# створення RLC-ланцюжку
#a = Vstep(10) + R(0.1) + C(0.4) + L(0.2, 0)
cct = lc.R(L) + lc.C(C)

# побудова графіку амплітуди напруги 
# на контурі в залежності від частоти
vt = linspace(0, 10, 1000)
#a.Isc(t).plot(vt)
cct.Isc(lc.t).plot(vt)

savefig('series-VRLC1-isc2.png')