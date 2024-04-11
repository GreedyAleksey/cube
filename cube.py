from math import *

def sgn(x):
    if x>0:return 1
    if x==0:return 0
    if x<0:return -1
    
print('Введите a,b,c,d')

aS, bS, cS, dS = map(float, input().split(','))

a = bS/aS
b = cS/aS
c = dS/aS

q = (a*a-3*b)/9
r = (2*a*a*a-9*a*b+27*c)/54
s = q*q*q-r*r

x1,x2,x3 = 0,0,0
i = 1j

print(q)
print(r)
print(s)

if s>0:
    f = (1/3)*acos(r/((q**3)**0.5))
    x1 = -2*q**0.5*cos(f)-(a/3)
    x2 = -2*q**0.5*cos(f+(2/3)*pi)-(a/3)
    x3 = -2*q**0.5*cos(f-(2/3)*pi)-(a/3)


if s<0:
    if q>0:
        f = (1/3)*acosh(abs(r)/((q**3)**0.5))
        x1 = -2*sgn(r)*q**0.5*cosh(f)-(a/3)
        x2 = sgn(r)*(q**0.5)*cosh(f)-(a/3)+i * 3**0.5 * q**0.5 * sinh(f)
        x3 = sgn(r)*(q**0.5)*cosh(f)-(a/3)-i * 3**0.5 * q**0.5 * sinh(f)


    if q<0:
        f = (1/3) * asinh(abs(r)/((abs(q)**3)**0.5))
        x1 = -2 * sgn(r) * (abs(q))**0.5 * sinh(f)-(a/3)
        x2 = sgn(r) * (abs(q))**0.5 * sinh(f)-(a/3) + i * 3**0.5 * (abs(q))**0.5 * cosh(f)
        x3 = sgn(r) * (abs(q))**0.5 * sinh(f)-(a/3) - i * 3**0.5 * (abs(q))**0.5 * cosh(f)

    if q==0:
        x1 = -(c-(a**3/27))**(1/3)-(a/3)
        x2 = -(a+x1)/2+(i/2) * (abs((a-3*x1)*(a+x1)-a*b))**0.5#!!!!
        x3 = -(a+x1)/2-(i/2) * (abs((a-3*x1)*(a+x1)-a*b))**0.5#!!!!

if s==0:
    x1 = -2 * r**(1/3) - (a/3)
    x2 = r**(1/3) - (a/3)

print('x1 = ', x1)
print('x2 = ', x2)
print('x3 = ', x3)


y1 = aS*x1**3+bS*x1**2+cS*x1+dS
y2 = aS*x2**3+bS*x2**2+cS*x2+dS
y3 = aS*x3**3+bS*x3**2+cS*x3+dS

print('y1 = ', y1)
print('y2 = ', y2)
print('y3 = ', y3)

if abs(y1)<0.000001 and abs(y2)<0.000001 and abs(y3)<0.000001:
    print('Погрешность мала => корни верные')
