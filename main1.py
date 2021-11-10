# python script to check whether the given number is perfect square or not
n=int(input())
p=n**(1/2)
for i in range(2):
                m=n/p
if(m==p):
            print("Perfect square Number")
else:
     print("Not perfect square Number")