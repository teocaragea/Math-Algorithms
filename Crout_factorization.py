#%%
import numpy as np
def verificare(a):
    n=len(a)
    if len(a)!=len(a[0]):
        return 0
    for i in range(1,n+1):
        if np.linalg.det(a[0:i,0:i])<1e-14:
            return 0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i][j]!=a[j][i]:
                return 0
    for i in range(0,n):
            if i>0:
                if a[i-1][i]==0:
                    return 0
            if i<n-1:
                if a[i+1][i]==0:
                    return 0
    return 1


def msd(a,b):
        n=len(a)
        x=[0]*n
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                b[i]-=a[i][j]*x[j]
            x[i]=b[i]/a[i][i]
        return x 
    

def msa(a,b):
    x=[0]*len(a)
    for i in range(0,len(a)):
        for j in range(0,i):
            b[i]-=a[i][j]*x[j]
        x[i]=b[i]/a[i][i]
    x=np.array(x)
    return x

def crout(a,b):
    n=len(a)
    l=np.zeros((n,n))
    u=np.identity(n)
    for i in range(0,n-1):
        l[i][i]=a[i,i]
        l[i+1,i]=a[i+1,i]
        u[i,i+1]=a[i,i+1]/a[i,i]
        a[i+1,i+1]-=l[i+1,i]*u[i,i+1]
    l[n-1,n-1]=a[n-1,n-1]
    print(l)
    print()
    print(u)
    print("Determinantul este",np.linalg.det(l)*np.linalg.det(u))
    x=msa(l,b)
    print(msd(l.transpose(),x))
    
    
a=np.array([[2.,-1.,0.,0.],[-1.,2.,-1.,0.],[0,-1.,2.,-1.],[0.,0.,-1.,2.]])
b=np.array([3.,4.,-4.,-3.])
if verificare(a):
    doolittle(a,b)
   