import numpy as np
import matplotlib.pyplot as plt
import math
import colorama

def sine(x):
    return (np.sin(x))

def plot(x, y):
    plt.plot(x, y, 'g-') 
    plt.grid(True)
    
# Limite dos eixos
# plt.axis([0, 10 * math.pi, -1, 1.01])

# Nome dos eixos
plt.ylabel('Eixo y')
plt.xlabel('Eixo x')

# Acentos devem ser usados com o código TeX
# plt.title(r'$\ddot{o}\acute{e}\grave{e}\hat{0} \breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)
# Titulo do grafico 
plt.title(r'$Gr\acute{a}fico$', fontsize=15)

def cardiod():
    t = np.arange(0, 2*math.pi, 0.01)
    r = 1 + np.cos(t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    plot(x, y)
    plt.show()

def butterfly():
    
    t = np.arange(0, 1000 * math.pi, 0.01)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np. power (np.sin(t/12), 5))
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np. power (np.sin(t/12), 5))
    plot(x, y)
    plt.show()

def tesla():
     
     x1 = np.arange(0, 2.0*math.pi, 0.01)
     x2 = np.arange(-2.0*math.pi/3.0, 4.0*math.pi/3.0, 0.01)
     x3 = np.arange(-4.0*math.pi/3.0, 2.0*math.pi/3.0, 0.01)
     y1 = np.sin(x1)
     y2 = np.sin(x2+ 2.0*math.pi/3.0)
     y3 = np.sin(x3 + 4.0*math.pi/3.0)
     plot(x1, y1)
     plot(x2, y2)
     plot(x3, y3)
     plt.show()
     
     
def lissajous_curve():
    a = 4.0
    b = 5.0
    kx = 3.0
    ky = 2.0
    t = np.arange(0, 2.0*math.pi, 0.01)
    x = a*np.cos(kx*t)
    y = b*np.sin(ky*t)
    plot(x, y)
    plt.show()
    
     
def begin():
    print('curves: \n 1 - cardiod \n 2 - butterfly curve \n 3 - tesla \n 4 - lissajous curve')
    curve = int(input('insert curve number: '))
    
    if (curve == 1):
        cardiod()
    elif (curve == 2):
        butterfly()
    elif (curve == 3):
        tesla()
    elif (curve == 4):
        lissajous_curve()
    else:
        print(colorama.Force.Red + colorama.Back.White + '\invalid input, try again')
        print(colorama.Style.RESET_ALL)
        begin()
if __name__ == '__main__':
    # x = np.arange(0, 10*math.pi, 0.01)
    # y = sine(x)
    # y = np.atrange(0)
    # y = math.sin(x)
        colorama.init()
        begin()
        


