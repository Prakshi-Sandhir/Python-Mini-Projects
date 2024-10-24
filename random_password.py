import random
import string
n=20
i=1
password=[] 
lower=int(input("enter how many lower case? "))
upper=int(input("enter how many upper case? "))
letter=int(input("enter how many letter case? "))
digits=int(input("enter how many digits case? "))

j=1
       
while j<=lower:
        a=random.choice(string.ascii_lowercase)
        password.append(a)
        j=j+1
j=1
while j<=upper:    
        b=random.choice(string.ascii_uppercase)
        password.append(b)
        j=j+1
j=1
while j<=letter:
        c=random.choice(string.punctuation)
        password.append(c)
        j=j+1
j=1
while j<=digits:
        d=random.choice(string.digits)
        password.append(d)
        j=j+1

random.shuffle(password)
print(''.join(password))
       

