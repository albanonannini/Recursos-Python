#y = mx + h
import math



x = [1.591,1.691,1.791,1.891,1.991]
y = [6.35,6.7,7.07,7.5,7.89]
error = [0.05,0.05,0.05,0.05,0.06]
N = len(x)

delta_x = x[N-1]-x[0]

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
R = 0

for i in range(N):
    A += x[i]*y[i]
    B += x[i]
    C += y[i]
    D += x[i]*x[i]

m = (N*A - B*C)/(N*D - B*B)
h = (D*C - B*A)/(N*D - B*B)
p = C/N

for i in range(N):
    E += (y[i] - p)*(y[i] - p)
    F += (y[i] - (h + m*x[i]))*(y[i] - (h + m*x[i]))

R = math.sqrt(1-F/E)



down_points = []
upper_points = []

for i in range(N):
    down_points.append(y[i] - error[i] - m*x[i])
    upper_points.append(y[i] + error[i] - m*x[i])

delta_h = (max(upper_points)-min(upper_points))/2
delta_m = 2*delta_h/delta_x

print('h = ',h,' pm ', delta_h,'; m = ', m,' pm ', delta_m,'; R = ', R)