me='mohammad'
mohammad=24
sister='mottahareh'
mottahareh=24
mother='zahra'
zahra=53
brother='amir'
amir=32
father='hasan'
hasan=60
location='iran west of tehran'
print(mother,brother,sister,me,father,location)
print('we trust in god')
if zahra<hasan:
    readme='my mother is so lonely'
    print(amir,mottahareh,mohammad)

readme
if mohammad>amir:
    readme='life is hell for you man'
    print(mother,father,sister,brother,location,'what i can to do')

readme
for mohammad in['empty','easy',5]:
    print(me)
    print(mohammad)
    print('hello how are you are you fine?')
    print(mohammad*3)

for mottahareh in range(1,9):
    print(mottahareh,mottahareh/mottahareh)
    print('everything is good very good is nice you know')

def a(a):
    print(a*a*a/a+a+a-a)

a(1)
a(32)
for b in ["saeed","maryam","karim",a(332)]:
    print("hello",b)
    print("i prouad to you mohammad")

def c(a,b,c):
    print(a+b+c)

c(1,2,3)
c("amir","ali","masod")

print(100%50)
print(100%25)
print(100%100)
print(100%75)
print(100%23)

for a in range (2,11):
    if 11%a==0:
        print("OK this is not a prime number at all")

m=11
if a in range (1,m):
    if m>10:
        print("hello world")

a=77
for s in range(2,a):
    if a%s==0:
        print("for",s,"this is a eaven number")

a=333
s=False
for d in range(2,a):
    if a%d==0:
        s=True
        if s:
            print("for",d,"this is a eaven number")
        else:
            print("this is a prome number")
            
def a(s):
    d=True
    for g in range (2,s):
        if s%g==0:
            d=False
    return d
for g in range (1,101):
    print(g,a(g))

def a(s):
    d=True
    for f in range(2,s):
        if s%f==0:
            d=False
    return d

for f in range (1,101):
    if a(f):
        print(f)

def a(s):
    d=True
    for f in range(2,int(s**0.5)+1):
        if s%f==0:
            d=False
    return d

f=0
for g in range(1,101):
    if a(g):
        f=f+1
        print(g,f)

def a(s):
    d=True
    for f in range(2,int(s**0.5)+1):
        if s%f==0:
            d=False
            break
    return d

f=0
for g in range(1,1001):
    if a(g):
        f=f+1
        print(a(g),f)

def a(s):
    d=True
    for f in range(2,int(s**0.5)+1):
        if s%f==0:
            d=False
            break
    return d

f=0
g=0
for h in range(1,1001):
    if a(h):
        f=f+1
        g=h
        print(h,a(h),f)

print(g)

def a(s) :
    print("Hello " + s)

a("hassan")

def a(s) :
    print("Hello " + s)

for q in ["hamid", "saeed", "mohsen", "nahid", "babak"] :
    a(q)


def a(s) :
    w = True
    for b in range (2, int(s**0.5)+1) :
        if s % b == 0 :
            w = False
            break
    return w
            
        
for q in range (1, 1001) :
    if a(q) :
        print(q)

def a(s) :
    return s % 3 == 0 or s % 5 == 0

w=0
for q in range (1, 1000) :
    if a(q) :
        w = w + q       
        print(w)

def a (s) :
    return s % 2 == 0

w = 0
e = 0
q = 1
while (e < 10) :
    r = e + q
    e = q
    q = r
    if a(e) :
        w = w + e
        print (w)

a = [1, 2, 3, "hassan", "morteza"]

a
a[0] 
a[2]
a[3] = "alireza"
a
len(a)
a.append("Hello")
a
a[1:4]
a[3:]
a[:3]
a
a.count("alireza")



a = []
for w in range(0, 33) :
    a.append(50)

while(a[2] < 100) :
    a[2] = a[2] + 1
    a[30] = a[30] - 1
    a

# Up by while(doing to get) and down by vibration(for)

a = []
for w in range(0, 33) :
    a.append(50)

for e in range(0, 50) :
    a[2] = a[2] + 1
    a[30] = a[30] - 1
    a



a = []
for w in range (0, 33) :
    a.append(50)

for w in range(0, 33) :
    a[w] = a[w] - 1
    a[30] = a[30] + 1
    a
    
# fix : random in below

import random
random.seed()
for w in range(0, 5) :
    random.randrange(1, 30) 

# fix : random in real story(jadi 15)


a = []
for w in range (0, 9) :
    a.append(5) 

import random
random.seed ()
for w in range (0, 9) :
    s = random.randrange(0, 9)
    a[w] = a[w] - 1
    a[s] = a[s] + 1
a

# fix : random in real story v2(jadi 15)

a = []
for w in range(0, 10) :
    a.append(50)

import random
random.seed 
for x in range(0, 25) :
    for w in range(0, 10) :
        s = random.randrange(0, 10) 
        a[w] = a[w] - 1
        a[s] = a[s] + 1
        print(w, s, a)

# fix : random 3 jadi 15

a = []
for w in range(4) :
    a.append(50)

import random
random.seed ()
for e in range(24) :
    for w in range(4) :
        s = random.randrange(4) 
        while(a[s] == 0) : 
            s = random.randrange(4)
        if a[w] == 0 :
            continue
        a[w] = a[w] - 25
        a[s] = a[s] + 25
        a

# if power jadi 15

import random
random.seed ()
q = [124] * 12
for r in range(2) :
    for w in range(12) :
        e=random.randrange(12)
        if q[w] > 0 :
            q[w] -= 90
            q[e] += 90
            q

# chart(matplotlib) jadi 16

import random
random.seed ()
a = [124] * 12
for w in range(24) :
    for e in range(12) :
        s = random.randrange(12)
        while(a[e] == 0) :
            a[e] = 0
        if a[e] < 1 :
            continue
        a[e] -= 70
        a[s] += 70
        a

import matplotlib.pyplot as plt
plt.bar(range(12), a)
plt.show()

# sort + chart for every changes jadi 16

import random 
import matplotlib.pyplot as plt
random.seed ()
a = [124] * 12
for w in range(24) :
    for e in range(12) :
        s = random.randrange(12)
        while(a[e] == 0) :
            a[e] = 0
        if a[e] < 1 :
            continue
        a[e] -= 70
        a[s] += 70
        a
        plt.bar(range(12), a)
        a.sort()
        plt.show()

# one random chart(not sort) jadi 16

import random 
import matplotlib.pyplot as plt
random.seed ()
a = [124] * 12
for w in range(24) :
    for e in range(12) :
        s = random.randrange(12)
        while(a[e] == 0) :
            a[e] = 0
        if a[e] < 1 :
            continue
        a[e] -= 70
        a[s] += 70
        a
        plt.bar(range(12), a)

plt.show()

# one sort chart jadi 16

import random 
import matplotlib.pyplot as plt
random.seed ()
a = [124] * 12
for w in range(24) :
    for e in range(12) :
        s = random.randrange(12)
        while(a[e] == 0) :
            a[e] = 0
        if a[e] < 1 :
            continue
        a[e] -= 70
        a[s] += 70
        a
        plt.bar(range(12), a)
        a.sort()

plt.show()

# sorted chart(refine sort) + reverse chart jadi 16

import matplotlib.pyplot as plt
import random 
random.seed ()
a = [124] * 12
for w in range(24) :
    for e in range(12) :
        s = random.randrange(12)
        while(a[e] == 0) :
            a[e] = 0
        if a[e] < 1 :
            continue
        a[e] -= 70
        a[s] += 70
        plt.bar(range(12), sorted(a, reverse=True))
plt.show()

            


    
