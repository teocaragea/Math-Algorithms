#%%
import numpy as np
import math
import matplotlib.pyplot as plt

def validmegpp(l,b):
    if len(l)!=len(l[0]): #verificam daca matricea e patratica.Din len(l)=nr de linii, len(l[0]) returneaza nr de coloane
        return 0
    if b.ndim!=1: # verificam ca matricea b sa fie doar o coloana
        return 0
    if len(l)!=b.size: # verificam compatibilitatea adica nr de linii din L sa fie egal cu coloanele din b
        return 0
   
    if abs(np.linalg.det(l))<(1e-14)**108: # functie predefinita sa calculam determinatu matricii b
        return 0
    return 1


def valid(l,b):# verificam conditiile metodei ascendente
    
    if len(l)!=len(l[0]): #verificam daca matricea e patratica.Din len(l)=nr de linii, len(l[0]) returneaza nr de coloane
        return 0
    
    n=len(l)# daca am ajuns aici matricea e patratica deci in n avem si nr de coloane si nr de linii
    for i in range(0,n):
        for j in range(0,n):# parcurgem matricea
            if j<i and abs(l[i][j])<(1e-14)**100: # ca matricea sa fie inferior triunghiulara trb sa fie totul 0 deasupra diagonalei principale
                return 0
            
            
    if b.ndim!=1: # verificam ca matricea b sa fie doar o coloana
        return 0
    if len(l)!=b.size: # verificam compatibilitatea adica nr de linii din L sa fie egal cu coloanele din b
       return 0
   
    if abs(np.linalg.det(l))<(1e-14)**104: # functie predefinita sa calculam determinatu matricii b
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
        X=np.array(x)
        return x
        
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
        return msd(a,b)##dupa ce am transformat matricea in una superior triunghiulara aplica metoda substitutiei descendente
    else:
        print("Nu se poate aplica megpp")
        
  
a=np.array([-5.,-3.4,-2.,-0.8,0,1.2,2.5,4.,5.,7.,8.5])
a1=np.ones(len(a))
a=np.vstack((a,a1))
a=a.T
t=np.transpose(a)
q=np.identity(len(a))
alfa=np.max(a)
alfa=alfa*1000
q=alfa*q
z=np.zeros((len(a[0]),len(a[0])))
l1=np.concatenate((q,a),axis=1)
l2=np.concatenate((t,z),axis=1)
L=np.concatenate((l1,l2),axis=0)
b=np.array([4.4,4.5,4.,3.6,3.9,3.8,3.5,2.5,1.2,0.5,-0.2])
o=np.zeros(len(a[0]))
b1=np.concatenate((b,o),axis=0)
sol=megpp(L,b1)
for i in range(0,len(a)-len(a[0])):
    sol[i]=sol[i]*alfa
plt.scatter(a.T[0], b)
plt.plot(a.T[0],a@sol[-len(a[0]):],"r")
plt.show()

###c si d
b=a.T[0]**2
a=np.vstack((b,a.T))
a=a.T
print(a)
t=np.transpose(a)
q=np.identity(len(a))
alfa=np.max(a)
alfa=alfa*1000
q=alfa*q
z=np.zeros((len(a[0]),len(a[0])))
l1=np.concatenate((q,a),axis=1)
l2=np.concatenate((t,z),axis=1)
L=np.concatenate((l1,l2),axis=0)
b=np.array([4.4,4.5,4.,3.6,3.9,3.8,3.5,2.5,1.2,0.5,-0.2])
o=np.zeros(len(a[0]))
b1=np.concatenate((b,o),axis=0)
sol=megpp(L,b1)
for i in range(0,len(a)-len(a[0])):
    sol[i]=sol[i]*alfa
print(a)
plt.scatter(a.T[0], b)
plt.plot(a.T[0],a@sol[-len(a[0]):],"r")
plt.show()

###d si e

b=a.T[1]**3
print(a.T[1])
a=np.vstack((b,a.T))
a=a.T
print(a)
t=np.transpose(a)
q=np.identity(len(a))
alfa=np.max(a)
alfa=alfa*1000
q=alfa*q
z=np.zeros((len(a[0]),len(a[0])))
l1=np.concatenate((q,a),axis=1)
l2=np.concatenate((t,z),axis=1)
L=np.concatenate((l1,l2),axis=0)
b=np.array([4.4,4.5,4.,3.6,3.9,3.8,3.5,2.5,1.2,0.5,-0.2])
o=np.zeros(len(a[0]))
b1=np.concatenate((b,o),axis=0)
sol=megpp(L,b1)
for i in range(0,len(a)-len(a[0])):
    sol[i]=sol[i]*alfa
print(a)
plt.scatter(a.T[0], b)
plt.plot(a.T[0],a@sol[-len(a[0]):],"r")
plt.show()
