import numpy as np
import csv
def printmat(M):
  n=len(M)
  for i in range (n):
    for j in range (n+1):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(round(float(M[i,j]),2),end=' \t')
    print("\n")
  print("\n")

def lu(O):
  n=len(O)
  A=[]
  B=[]
  X=[]
  Y=[]
  for i in range (0,n):
    r1=[]
    r2=[]
    for j in range (0,n):
      if i==0:
        r1.append(O[i,j])
      else:
        r1.append(0.0)
      if j==i:
        r2.append(1.0)
      else:
        r2.append(0.0)
    A.append(r1)
    B.append(r2)
    X.append(0.0)
  A=np.matrix(A)
  B=np.matrix(B)
  X=np.matrix(X)
  Y=np.matrix(X)
  M=np.matrix(O)
  if(M[0,0]==0):
    for j in range (0,n):
      if M[j,0]!=0:
        for k in range (0,n+1):
          swap=float(M[j,k])
          M[j,k]=float(M[0,k])
          M[0,k]=float(swap)
  print("The new matrix after swapping (as the first element in the input matrix is 0):")
  printmat(M)
  for i in range (0,n):
    for j in range (0,n):
      sum1=0.0
      sum2=0.0
      if j>=i:
        for k in range (0,n):
          if k!=i:
            sum1+=(B[i,k]*A[k,j])
        A[i,j]= M[i,j]-sum1
      if j<i:
        for l in range (0,n):
          if l!=j:
            sum2+=(B[i,l]*A[l,j])
        B[i,j]= (M[i,j]-sum2)/A[j,j] 
  for i in range (0,n):
    s2=0.0
    for j in range (0,i):
        s2=s2+(B[i,j]*Y[0,j])
    Y[0,i]=((M[i,n]-s2)/B[i,i])
  for i in range (n,0,-1):
        s3=0.0
        k=i-1
        for j in range (k+1,n):
            s3= s3+ (A[k,j]*X[0,j])
        X[0,k]=((Y[0,k]-s3)/A[k,k])
  return X

def input(path):
  i=0
  j=0
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))

def main(q):
    q=str(q)
    A=np.matrix(input(q))
    #lu(A)
    print("The input matrix is : \n")
    printmat(A)
    B=lu(A)
    n=len(A)
    print("The solution of the given linear equations using LU decomposition method is : \n")
    for i in range (0,n):
        print("x"+str(i+1)+" = "+str(B[0,i]))
    return
