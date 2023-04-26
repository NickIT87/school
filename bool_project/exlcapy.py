


from lcapy import R, C, L

((R(1) + L(2)) | C(3)).draw()

print(((R(1) + L(2)) | C(3)).netlist())


from lcapy import Circuit
import matplotlib.pyplot as plt
a = Circuit("""
V 1 0 {v(t)}; down
R1 1 2; right
L 2 3; right=1.5, i=i_L
R2 3 0_3; down=1.5, i=i_{R2}, v=v_{R2}
W 0 0_3; right
W 3 3_a; right
C 3_a 0_4; down, i=i_C, v=v_C
W 0_3 0_4; right""")


from lcapy import Vstep, R, L, C, t
from matplotlib.pyplot import savefig
from numpy import linspace

a = Vstep(10) + R(0.1) + C(0.4) + L(0.2, 0)

vt = linspace(0, 10, 1000)
a.Isc(t).plot(vt)

savefig('series-VRLC1-isc.png')