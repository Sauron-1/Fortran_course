'''
This is a temporary script used for programming.
Missing this script will not affect the project.
'''
from numpy import *
import re
import sympy as sp
from sympy.printing import latex
import matplotlib.pyplot as plt

L = sp.symbols('L')
Re = sp.symbols('Re')
B0 = sp.symbols('B0')

L_v = 6.6
Re_v = 6376e3
B0_v = 3.12e-5

theta = sp.symbols('theta')
kai = sp.cos(theta)

s = L*Re/2 * (kai*sp.sqrt(1+3*kai**2) + 1/sp.sqrt(3)*sp.log(sp.sqrt(1+3*kai**2)+sp.sqrt(3)*kai))

B = B0/L**3 * sp.sqrt(1+3*kai**2) / (sp.sin(theta))**6

r = L*Re*sp.sin(theta)**2
h = r*sp.sin(theta)

e_B = sp.log(h**2*B)

with open('o_B.txt', 'w') as f:
    f.write(str(sp.diff(e_B, theta)/sp.diff(s, theta).simplify()))
with open('ps_ptheta.txt', 'w') as f:
    f.write(str(sp.diff(s, theta).simplify()))
with open('ps_ptheta_2.txt', 'w') as f:
    f.write(str(sp.diff(s, theta, 2).simplify()))
with open('ph_ptheta.txt', 'w') as f:
    f.write(str(sp.diff(h, theta).simplify()))
with open('ph_ptheta_2.txt', 'w') as f:
    f.write(str(sp.diff(h, theta, 2).simplify()))

'''
value_dict = {L:L_v, Re:Re_v, B0:B0_v}
thetas_v = linspace(arcsin(-sqrt(1/L_v)), arcsin(sqrt(1/L_v)), 200)
ds_dthetas = sp.diff(s, theta)
ds_dthetas_2 = sp.diff(s, theta, 2)
o_B = sp.diff(e_B, theta)/ds_dthetas
ds_dthetas_v = eval(re.sub('theta', 'thetas_v', str(ds_dthetas.subs(value_dict))))
ds_dthetas_2_v = eval(re.sub('theta', 'thetas_v', str(ds_dthetas_2.subs(value_dict))))
h_v = eval(re.sub('theta', 'thetas_v', str(h.subs(value_dict))))
#plt.plot(thetas_v, ds_dthetas_v/L_v/Re_v)
#plt.plot(thetas_v, ds_dthetas_2_v/L_v/Re_v)
#plt.show()
#plt.plot(thetas_v, ds_dthetas_2_v/ds_dthetas_v)
#plt.plot(thetas_v, sin(thetas_v)/ds_dthetas_v)
#plt.show()
plt.text(0.5, 0.5, 
        #'$%s$'%(latex((ds_dthetas_2/ds_dthetas - o_B*ds_dthetas).simplify())), 
        '$%s$'%(latex(o_B.simplify())),
        size=20)
plt.show()
'''
