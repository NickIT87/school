import lcapy as lc

L = 1 # индуктивность в Гн
C = 1e-6 # емкость в Ф

# создание RLC-цепочки
cct = lc.R(L) + lc.C(C)

# построение графика амплитуды напряжения на контуре в зависимости от частоты

from matplotlib.pyplot import savefig
from numpy import linspace


vt = linspace(0, 10, 1000)
cct.Isc(lc.t).plot(vt)

savefig('series-VRLC1-isc.png')