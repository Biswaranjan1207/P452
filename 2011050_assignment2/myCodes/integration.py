import math
#import lcg as l

def no_simp(a,b):
    n=math.ceil(((2*(b-a)**5)/(15*10**-4))**(1/4))
    if n%2==0:
        n=n
    else:
        n+=1
    print("The value of N for Simpson:",n)
    return n

def no_mid(a,b):
    n=math.ceil((((b-a)**3)/(12*10**-4))**(1/2))
    print("The value of N for mid pt rule:",n)
    return n
def no_trap(a,b):
    n=math.ceil((((b-a)**3)/(6*10**-4))**(1/2))
    print("The value of N for trapezoidal rule:",n)
    return n
    
def m_integ(f,a,b,N):
    #N=no_mid(a,b)
    h=(b-a)/N
    x=a+h/2
    sum=0.0
    while x<=b:
        sum+=h*f(x)
        x+=h
    return sum
def t_integ(f,a,b,N):
    #N=no_trap(a,b)
    h=(b-a)/N
    sum=f(a)+f(b)
    for i in range (1,N):
        k=a+i*h
        sum+=2*f(k)
    sum*=(h/2)
    return sum

def simp(f,a,b,N):
    #N=no_simp(a,b)
    h=(b-a)/N
    sum=f(a)+f(b)
    for i in range(1,N):
        k=a+i*h
        if i%2==0:
            sum+=2*f(k)
        else:
            sum+=4*f(k)
    sum*=(h/3)
    return sum
def moncar(f1,a,b,N):
    sum=0
    sqr_sum=0
    r=l.lc(10,N)
    for i in range(N):
        x=a+(b-a)*r[i]
        sum+=f1(x)
        sqr_sum+=f1(x)**2
    integral=(b-a)*sum/N
    sigma=((1/N)*sqr_sum-(sum/N)**2)**0.5
    return integral
 

