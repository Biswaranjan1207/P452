#Non linear equations using regula falsi method

def refal(f,a0,b0):
    iter=0
    h=0.1
    if f(a0)*f(b0)>0:
        print("The initial guess interval doesn't contain the required root")
        print("Bracketing needs to be done...")
        a0=a0-h*a0
    c0=b0-((b0-a0)*f(b0))/(f(b0)-f(a0))
    while abs(f(c0))>10**-6:
        c0=b0-((b0-a0)*f(b0))/(f(b0)-f(a0))
        if f(c0)*f(a0)<0:
            b0=c0
        elif f(c0)*f(b0)<0:
            a0=c0
        iter+=1
    print("No of iterations for regula falsi method:",iter+1)
    print("Required root using Regula falsi method:",round(c0,6))

    