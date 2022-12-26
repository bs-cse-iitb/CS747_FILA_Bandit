from random import uniform

class Bandit:
    def __init__(self,x,y):
        self.p1=x
        self.p2=y
    def get_reward(self):
        return(uniform(self.p1,self.p2))



a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
d=float(input("d = "))
N=10000

if(not(0<=a<c<b<d<=1)):
    print("Invalid Input")
    exit()

arm1=Bandit(a,b)
arm2=Bandit(c,d)

print(arm1)
print(arm2)

print("For N="+str(N))
total=0
for i in range(N):
    A1=arm1.get_reward()
    A2=arm2.get_reward()

    val=A1+A2
    if(A2<=A1):
        for j in range(20):
            val+=arm1.get_reward()
    else:
        for j in range(20):
            val+=arm2.get_reward()

    total+=val

result=total/N

################################################

p=(b-c)*(b-c)/(2*(d-c)*(b-a))
Earm1=(21*(a+b)+(c+d))/2
Earm2=((a+b)+21*(c+d))/2
expResult=p*Earm1+(1-p)*Earm2

print("Experimental Result:\t"+str(result))
print("Expected Result:\t"+str(expResult))
