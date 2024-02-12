
# Fixed Point Iteration Method
# Importing math to use sqrt function

# Implementing Fixed Point Iteration Method
def fixedPointIteration(f,g,x0, e, N):
    print('\n*** FIXED POINT ITERATION ***')
    count = 1
    #starting the iteration count
    x1=g(x0)
    #checking the condition when root converges to the exact root
    while abs(x1-x0) > e:
        x0=x1
        x1 = g(x0)
        count += 1
        if count > N:
            print('\nNot Convergent.')
            break
    print("Total number of iterations:", count)
    print('Required root of the given non-linear eqn is:',round(x1,4),'\n')




