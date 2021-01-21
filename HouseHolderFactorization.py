
#%%ex2
def verificare(a):
    if len(a)<len(a[0]):
        return 0
    if np.linalg.det(a.T@a)==0:
        return 0
    return 1

def qr_householder(A):
    m,n=np.shape(A)
    Q=np.identity(max(m,n))
    R=A
    for j in range(min(m,n)):
        a = R[j:, j]
        norm = np.linalg.norm(a)
        v1 = a[0] -np.sign(a[0])  * norm
        v = a / v1
        v[0] = 1
        alfa = -np.sign(a[0]) * v1 / norm
        R[j:, :] = R[j:, :] - alfa * np.outer(v, v).dot(R[j:, :])
        Q[:, j:] = Q[:, j:] - alfa * Q[:, j:].dot(np.outer(v, v))
    return Q, R


a=np.array([[0.1,0.1],[0.17,0.11],[2.02,1.29]]) 
if verificare(a)==1:
   q,r=qr_householder(a)
else:
    print("nu se poate factoriza")
print(q)
print()
print(r)
print()
print(q@r)#=a
print()
print(q@q.T)#=Im

i=np.identity(len(q))
q=q-i
m=0
for i in range(0,len(a)):
    for j in range(0,len(q[0])):
        m+=q[i][j]**2
print(m)
x=[0]*13
y=[0]*13
for n in range(2,13):
    h=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            h[i][j]=1/(i+j+1)
    q,r=raf_qr(h,1)
    x[n]=n
    y[n]=-math.log10(np.linalg.norm(np.identity(n)-q@q.T,'fro'))
plt.plot(x[2:],y[2:])
#%%ex3

def msd(a,b):##functia pt metoda substitutiei descendente
        n=len(a)
        x=[0]*n#initializam vectorul in care retinem solutiile, va avea aceeasi dimensiune cu n(numrul de linii sau coloane)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                b[i]-=a[i][j]*x[j]
            x[i]=b[i]/a[i][i]
        return x #returnam sub forma de lista pt a pastra solutia
    
def verificare(a):
    if len(a)<len(a[0]):
        return 0
    if np.linalg.det(a.T@a)==0:
        return 0
    return 1

def qr_householder(A):
    m,n=np.shape(A)
    Q=np.identity(max(m,n))
    R=A
    for j in range(min(m,n)):
        a = R[j:, j]
        norm = np.linalg.norm(a)
        v1 = a[0] -np.sign(a[0])  * norm
        v = a / v1
        v[0] = 1
        alfa = -np.sign(a[0]) * v1 / norm
        R[j:, :] = R[j:, :] - alfa * np.outer(v, v).dot(R[j:, :])
        Q[:, j:] = Q[:, j:] - alfa * Q[:, j:].dot(np.outer(v, v))
    return Q, R


a=np.array([[0.1,0.1],[0.17,0.11],[2.02,1.29]]) 
if verificare(a)==1:
   q,r=qr_householder(a)
else:
    print("nu se poate factoriza")


x=msd(r[1:,:],q.T@b)
print(x)
print()
r=a@x-b
print(r)
print()
print(np.linalg.norm(r))




        
        

