def f(x,y):
    return (x)
def pred(x0,y0,h,x):
    y1=0
    y2=0
    while x0<x:
        x1=float(x0)
        y1=float(y0)
        y2 = y0 + h*f(x0,y0)
        x0 = x0 + h
        y0 = y1 + h*((f(x0,y2)+f(x1,y1))/2)
    print(y0)
pred(0,0,0.025,0.1)