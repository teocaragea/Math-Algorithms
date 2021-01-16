#%%inversa unei matrici

import numpy as np

def msd(a,b):##functia pt metoda substitutiei descendente
        n=len(a)
        x=[0]*n#initializam vectorul in care retinem solutiile, va avea aceeasi dimensiune cu n(numrul de linii sau coloane)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                b[i]-=a[i][j]*x[j]
            x[i]=b[i]/a[i][i]
        return x #returnam sub forma de lista pt a pastra solutia
        

def inversa(a,d):##algoritmul pt aflarea inversei folosind megfp putin modificat
    n=len(a)#numarul de linii
    for k in range(0,n-1):
        b=d[k]      
        for i in range(k+1,n):
            m=a[i][k]/a[k][k]# calculanm pivotul
            for x in range(0,n):
                d[i][x]-=m*d[k][x]##scadem liniile corespunzatoare din In
            for j in range(k+1,n):
                a[i][j]=a[i][j]-m*a[k][j]
            a[i][k]=0
    d=np.transpose(d)#am facut transpusa ca sa pot da ca parametru la msd prima linie, a 2a etc in loc de coloane
    sol=[]# memoram solutiile
    for k in range(0,n):
      sol.append(msd(a,d[k]))
    a=np.array(sol)
    print(np.transpose(sol))##afisam transpusa deoarce rezultatele trebuiesc puse pe coloane
        
    

a=np.array([[1.,2.,0.],[2.,1.,-1.],[3.,1.,1.]])
b=np.identity(len(a))##initializam b cu In
inversa(a,b)