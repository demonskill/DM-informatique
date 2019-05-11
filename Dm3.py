#Question I.2
def smul(n,L) :
    T=[]
    for i in range(len(L)) :
        T.append(n*L[i])
    return T

#Question I.3 a)
def vsom(L_1,L_2) :
    T=[]
    for i in range(len(L_1)) :
        T.append(L_1[i] +L_2[i])
    return T
    
#Question I.3 b)
def vdiff(L_1,L_2) :
    T=[]
    for i in range(len(L_1)) :
        T.append(L_1[i] -L_2[i])
    return T

#Question II.2.2
def euler(f,t_min,t_max,n,z0,y0) :
    h=(t_max -t_min)/(n-1)
    T=[]
    for i in range(n) :
        T.append(t_min + i*h)
    z=z_0
    y=y_0
    Z=[z_0]
    Y=[y_0]
    for i in range(len(T)) :
        z,y= z + (T[i+1] - T[i])*f(y),y + (T[i+1] - T[i]) * z
        Z.append(z)
        Y.append(y)
    return(Z,Y)

#Question II.3.1
def verlet(f,t_min,t_max,n,z0,y0) :
    h=(t_max -t_min)/(n-1)
    T=[]
    for i in range(n) :
        T.append(t_min + i*h)
    z=z_0
    y=y_0
    Z=[z_0]
    Y=[y_0]
    for i in range(len(T)) :
        y= y + h*z + (h**2)/2*f(y_i)
        z= z+ h/2*(f(Y[-1])+f(y))
        Z.append(z)
        Y.append(y)
    return(Z,Y)

#Question III.1.2
def force2(m1,p1,m2,p2) :
    G=6.67e-11
    p1p2= vdiff(p2,p1)
    r=sqrt(p1p2[0]**2+p1p2[1]**2+p1p2[2]**2)
    return(smul(G*m1*m2/(r**3),p1p2))


#Question III.1.3
def forceN(j,m,pos):
    m1=m[j]
    p1=pos[j]
    F=[0,0,0]
    for i in range(len(m)) :
        if i!=j :
            vsom(F,force2(m1,p1,m[i],pos[i]))
    return F

#Question III.2.2
def euler_3d(f,t_min,t_max,n,z0,y0) :
    h=(t_max -t_min)/(n-1)
    T=[]
    for i in range(n) :
        T.append(t_min + i*h)
    z=z_0
    y=y_0
    Z=[z_0]
    Y=[y_0]
    for i in range(len(T)) :
        z,y= vsom(z, smul((T[i+1] - T[i]),f(y))),vsom(y, smul((T[i+1] - T[i]), z))
        Z.append(z)
        Y.append(y)
    return(Z,Y)
def pos_suiv(m, pos, vit,h) :
    pos2=[]
    vit2=[]
    def f(y) :
        return forceN(y,m,pos)
    for i in range(len(pos)) :
        solution=euler_3d(f,0,h,2,vit[i],pos[i])
        pos2.append(solution[1][1])
        vit2.append(solution[0][1])
    return(vit2,pos2)

#Question III.2.3
def verlet_3d(f,t_min,t_max,n,z0,y0) :
    h=(t_max -t_min)/(n-1)
    T=[]
    for i in range(n) :
        T.append(t_min + i*h)
    z=z_0
    y=y_0
    Z=[z_0]
    Y=[y_0]
    for i in range(len(T)) :
        y= vsom(vsom( y ,smul(h,z)),smul((h**2)/2,f(y)))
        z= vsom(z, smul(h/2,vsom(f(Y[-1]),f(y))))
        Z.append(z)
        Y.append(y)
    return(Z,Y)
def etat_suiv(m,pos,vit,h) :
    pos2=[]
    vit2=[]
    def f(j) :
        return (forceN(j,m,pos)/m[j])
    for i in range(len(pos)) :
        solution=verlet_3d(f,0,h,2,vit[i],pos[i])
        vit2.append(solution[0][1])
        pos2.append(solution[1][1])
    return(vit2,pos2)

#Question III.2.6
def simulation_verlet(deltat,n) :
    pos=p0
    vit=v0
    position=[p0]
    for i in range(n) :
        solutions=etat_suiv(m,pos,vit,deltat)
        vit=solutions[0]
        pos=solutions[1]
        position.append(pos)
    return position
