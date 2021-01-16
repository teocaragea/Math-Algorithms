#%%LUFP
import numpy as np
import scipy.linalg
def validare(a):
    if np.linalg.det(a)==0:
        return 0
    if len(a)!=len(a[0]):
        return 0
    return 1


def valid(l,b):# verificam conditiile metodei ascendente
    
    if len(l)!=len(l[0]): #verificam daca matricea e patratica.Din len(l)=nr de linii, len(l[0]) returneaza nr de coloane
        return 0
    
    n=len(l)# daca am ajuns aici matricea e patratica deci in n avem si nr de coloane si nr de linii
    for i in range(0,n):
        for j in range(i+1,n):# parcurgem matricea
            if l[i][j]!=0: # ca matricea sa fie inferior triunghiulara trb sa fie totul 0 deasupra diagonalei principale
                return 0
            
            
    if b.ndim!=1: # verificam ca matricea b sa fie doar o coloana
        return 0
    if len(l)!=b.size: # verificam compatibilitatea adica nr de linii din L sa fie egal cu coloanele din b
       return 0
   
    if np.linalg.det(l)==0: # functie predefinita sa calculam determinatu matricii b
        return 0
    return 1

def LUFP(a):
    if validare(a)==1:
        n=len(a)
        P=np.identity(n)
        L=np.zeros((n,n))
        u=np.zeros((n,n))
       
        for k in range(0,n):
            L[k][k]=1
            l=0
            max=0
            for i in range(0,k+1):
                if abs(a[k][i])>max:
                    max=abs(a[k][i])
                    l=i
            p=np.identity(n)
            p[[l,k]]=p[[k,l]]
            a[[l,k]]=a[[k,l]]
            L[[k,l],:k] = L[[l,k],:k]
            P=p@P
            u[k][k]=a[k][k]
            for i in range(k+1,n):
                L[i][k]=a[i][k]/u[k][k]
                u[k][i]=a[k][i]
            for i in range(k+1,n):
                for j in range(k+1,n):
                    a[i][j]-=L[i][k]*u[k][j]
        return L,u,P
    else:
         print("Nu se poate factoriza")
        

a=np.array([[0.,0.,-1.,1.],[1,1,-1,2],[-1.,-1.,2.,0.],[1.,2.,0.,2.]])
n=len(a)
l=np.zeros((n,n))
u=np.zeros((n,n))
p=np.zeros((n,n))
p,l,u=scipy.linalg.lu(a)
print(l)
print()
print(u)
print()
print(p)
l,u,p=LUFP(a)
print()
print(l)
print()
print(u)
print()
print(p)