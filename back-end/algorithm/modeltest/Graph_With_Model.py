import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import optimize as op

x = np.array([0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.46,0.47,0.48,0.49,
              0.5,0.51,0.52,0.53,0.54,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9])
y = np.array([50,54,65,73,70,75,80,82,84,86.8,88.5,92,92.5,91.5,90.5,89.7,88.6,
              88,80,76,70,65,63,60,55])

def func(x,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    return o*x**15+p*x**14+m*x**13+n*x**12+l*x**11+j*x**10+k*x**9+h*x**8+i*x**7+a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x**1+g
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p= curve_fit(func, x, y)[0]


yresult = func(x,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p) #拟合y值

#绘图
# plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yresult, 'r')
plt.xlabel('λ')
plt.ylabel('Average similarity')
plt.xlim(0,1)
plt.ylim(0,100)
plt.title('Average similarity with λ')
# plt.show()
plt.savefig("./λ_graph")
