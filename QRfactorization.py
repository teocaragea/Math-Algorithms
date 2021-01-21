#%%
import numpy as np
def verificare(a):
    if len(a)<len(a[0]):
        return 0
    if np.linalg.det(a.T@a)==0:
        return 0
    return 1
def factorizareQR(a):
    r=np.zeros((len(a[0]),len(a[0])))
    q=np.zeros((len(a),len(a[0])))
    for j in range(0,len(a[0])):
        q[:,j]=a[:,j]
        for i in range(0,j):
            r[i][j]=q[:,i].T@a[:,j]
            q[:,j]=q[:,j]-q[:,i]*r[i][j]
        r[j][j]=np.linalg.norm(q[:,j])
        q[:,j]=q[:,j]/r[j][j]
    return(q,r)


a=np.array([[0.1,0.1],[0.17,0.11],[2.02,1.29]])
b=np.array([0.26,0.28,3.31])
if verificare(a)==1:
    q,r=factorizareQR(a)
else:
    print("Matricea nu se poate factoriza")
print(q)
print()
print(r)
