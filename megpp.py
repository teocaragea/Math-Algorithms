#%%megpp
import numpy as np


def validmegpp(l,b):
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

def megpp(a,b):##algoritmul de megpp prezentat
    if validmegpp(a,b)==1:##verificam compatibilitatea
        n=len(a)#matricea fiind patratica n e si nr de linii si de coloane
        for k in range(0,n-1):
            max=0
            for i in range(k,n):
                if max<abs(a[i][k]):
                    max=abs(a[i][k])
                    l=i
            a[[l, k]] = a[[k, l]]
            b[[l, k]] = b[[k, l]]
            for i in range(k+1,n):
                m=a[i][k]/a[k][k]
                b[i]=b[i]-m*b[k]
                for j in range(k+1,n):
                    a[i][j]=a[i][j]-m*a[k][j]
                a[i][k]=0        
        
        msd(a,b)##dupa ce am transformat matricea in una superior triunghiulara aplica metoda substitutiei descendente
    else:
        print("Nu se poate aplica megpp")

        
a=np.array([[1.,2.,1.],[2.,2.,3.],[-1.,-3.,1.]])
b=np.array([0.,3.,3.])
megpp(a,b)