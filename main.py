import math
import matplotlib.pyplot as plt
g = 9.8
dt = 1e-14
e = 1.6*1e-19
Me = 9.1*1e-31
R0 = 9*1e-2
r0 = 4*1e-2
Umin = 0
Umax = 100
Vx = 6*1e6
L = 17*1e-2
T = L/Vx
ts = []
ys = []
xs = []
Vys = []
Ays = []
Vy = 0
while(Umax-Umin>0.001):
    ts = []
    ys = []
    xs = []
    Vys = []
    Ays = []
    U = (Umax+Umin)/2
    r = (R0 + r0) / 2
    Const = U*e/(Me*math.log(R0/r0))
    a = Const/r + g
    Vy = 0
    t = 0
    x = 0
    while t < T:
        ys.append(r)
        xs.append(x)
        ts.append(t)
        Vys.append(Vy)
        Ays.append(a)
        dr = Vy*dt+(a*dt**2)/2
        Vy +=a*dt
        r = r-dr
        a = Const/r+g
        t += dt
        x +=Vx*dt
    if r < r0 :
        Umax = U
    else:
        Umin = U
print("U = "+str(int(Umin*100)/100)+"B")
print("t = "+str(t))
print("V = "+str(math.sqrt(Vy**2+Vx**2)))
plt.plot(xs,ys)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.plot(ts,Vys)
plt.ylabel("Vy")
plt.xlabel("t")
plt.show()
plt.plot(ts,Ays)
plt.ylabel("Ay")
plt.xlabel("t")
plt.show()
plt.plot(ts,ys)
plt.ylabel("y")
plt.xlabel("t")
plt.show()

