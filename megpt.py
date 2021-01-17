#%%
import numpy as np
def validmegppt(l,b):
    if len(l)!=len(l[0]): #verificam daca matricea e patratica.Din len(l)=nr de linii, len(l[0]) returneaza nr de coloane
        return 0
    if b.ndim!=1: # verificam ca matricea b sa fie doar o coloana
        return 0
    if len(l)!=b.size: # verificam compatibilitatea adica nr de linii din L sa fie egal cu coloanele din b
       return 0
   
    if abs(np.linalg.det(l))<1e-14: # functie predefinita sa calculam determinatu matricii b
        return 0
    return 1

def valid(l,b):# verificam conditiile metodei ascendente
    
    if len(l)!=len(l[0]): #verificam daca matricea e patratica.Din len(l)=nr de linii, len(l[0]) returneaza nr de coloane
        return 0
    
    n=len(l)# daca am ajuns aici matricea e patratica deci in n avem si nr de coloane si nr de linii
    for i in range(0,n):
        for j in range(0,n):# parcurgem matricea
            if j<i and l[i][j]!=0: # ca matricea sa fie inferior triunghiulara trb sa fie totul 0 deasupra diagonalei principale
                return 0
            
            
    if b.ndim!=1: # verificam ca matricea b sa fie doar o coloana
        return 0
    if len(l)!=b.size: # verificam compatibilitatea adica nr de linii din L sa fie egal cu coloanele din b
       return 0
   
    if np.linalg.det(l)==0: # functie predefinita sa calculam determinatu matricii b
        return 0
    return 1

def msd(a,b,q):
    if valid(a,b)==1:#verificam compatibilitatea
        n=len(a)
        x=[0]*n#initializam vectorul in care retinem solutiile, va avea aceeasi dimensiune cu n(numrul de linii sau coloane)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                b[i]-=a[i][j]*x[j]
            x[i]=b[i]/a[i][i]
        x=x@q
        print(x)
        
    else:
        print("Sistem incompatibil")

def megppt(a,b):
    n=len(a)
    qfinal=np.identity(n)
    for k in range(0,n-1):
        max=0
        for l in range(k,n):
           for m in range(k,n):
               if abs(a[l][m])>max:
                   max=abs(a[l][m])
                   l1=l
                   m1=m
                   
        a[[l1, k]] = a[[k, l1]]
        b[[l1, k]] = b[[k, l1]]
        q=np.identity(n)
        q[[m1,k]]=q[[k,m1]]
        qfinal=qfinal@q
        a=a@q
        for i in range(k+1,n):
            m=a[i][k]/a[k][k]
            b[i]-=m*b[k]
            for j in range(k+1,n):
                a[i][j]-=m*a[k][j]
            a[i][k]=0
    
    msd(a,b,qfinal)
        
a=np.array([[1.,2.,1.],[2.,2.,3.],[-1.,-3.,1.]])
b=np.array([0.,3.,3.])
if validmegppt(a,b)==1:
  megppt(a,b)
else:
  print("Nu se poate aplica megppt")    