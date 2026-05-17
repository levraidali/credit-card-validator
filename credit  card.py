from numpy import*

def credit_card():
    n=0
    c=input("donnez votre numero de carte")
    while not(c.isdigit()) or len(c)!=16:
        c=input("numero de carte invalide")
    for i in range(len(c)):
        t.append(c[i])
    for i in range(16):
        if i%2==0:
            t[i]=str(int(t[i])*2)
    for j in range(16):
        if j%2==0:
            if int(t[j])>=10:
                t[j]=somme(t[j])
            else:
                t[j]=t[j]
    for i in range(16):
        n=n+int(t[i])
    if n%10==0:
        print("carte valide")
    else:
        print("numero de carte invalide donnez un numero valide")
    
    
    
def somme(a):
    A=int(a)
    
    return str(A%10+A//10)
    
t=[]
credit_card()
print(t)
    