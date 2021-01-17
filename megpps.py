#%%MEGGPS
import numpy as np
def validmegpps(l,b):
    if len(l)!=len(l[0]): #verificam daca matricea e patratica.Din len(l)=nr de linii, len(l[0]) returneaza nr de coloane
        return 0
    if b.ndim!=1: # verificam ca matricea b sa fie doar o coloana
        return 0
    if len(l)!=b.size: # verificam compatibilitatea adica nr de linii din L sa fie egal cu coloanele din b
       return 0
   
    if np.linalg.det(l)==0: # functie predefinita sa calculam determinatu matricii b
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

def msd(a,b):
    if valid(a,b)==1:#verificam compatibilitatea
        n=len(a)
        x=[0]*n#initializam vectorul in care retinem solutiile, va avea aceeasi dimensiune cu n(numrul de linii sau coloane)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                b[i]-=a[i][j]*x[j]
            x[i]=b[i]/a[i][i]
        print(x)
        
    else:
        print("Sistem incompatibil")
def MEGPPS( U , b) :
    n= len(U)
    for k in range (0 , n-1):
       for i in range(k,n):
           maxi=0
           for j in range(k,n):
               if abs(U[i][j])>maxi:
                   maxi=U[i][j]
                   s=j
                   a1=U[i][k]/s
    
       for i in range(k,n):
            if abs(U[i][k])>maxi:
                maxi=U[i][k]
                l=i
                U[[l,k]]=U[[k,l]]
                b[[l,k]]=b[[k,l]] 
            
            
            for i in range(k+1 , n) :
                m = U[i,k] / U[k,k]
                b[i] = b[i] - m * b[k]
                for j in range(k+1,n):
                     U[i,j] = U[i,j] - m * U[k,j]
       U[i,k] = 0
    return msd(a,b)

a=np.array([[1,2,3],[2,6,6],[1,6,10]])
b=np.array([6,14,17])
if validmegpps(a,b)==1:
    MEGPPS(a,b)
else:
    print("Nu se poate aplica MEGGPS")