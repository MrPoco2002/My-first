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

# refactor : dictionary = {} also () and [] jadi 17

a = ()
a
s = []
s
d = {}
d
a = (1, 2, 3, 4, 5, "hassan", "karim")
a
s = [2, 3, 4, 5, 6, "kamal", "masod"]
s
s.append("hesam")
s
s[2] = 7
s
s[3] = "hamington"
s
d = {1, 2, 3, 4, 5, 6, "julasy", "happyness", "sadness"}
d
d = {1 : "q", 2 : "w", 3 : "e", "julast" : "worker", "happyness" : 7}
d
d[7] = 8
d
d[8] = "hamid"
d
d["masod"] = 7
d
d["hamed"] = "neda"
d
d[2]
d
d.get(3)
d.get("julast")
d.get("hassan", "none")
d.keys()
d.values()
"ali" in d
"happyness" in d
"worker" in d
for w in d :
    print(w)
for w in d.items() :
    print(w)
for k, v in d.items() :
    print("key is", k)
    print("value is", v)

# Classes jadi 18 

a = "74"
a[0]
a[1]
a(int)
a(str)
a.capitalize()
a.zfill(7)

#pincode quastion jadi 18(Way 1)

for a in range(10) :
    for s in range(10) :
        for d in range(10) :
            for f in range(10) :
                for g in range(10) :
                    if a + s + d + f + g == 30 and d + g == 14 and s + d == 10 and f - 1 == s and a + 1 == s * 2 :
                        print(a, s, d, f, g)

# Pincode quastion jadi 18(Way 2) 

for w in range(100000) :
    q = str(w).zfill(5)
    e = {}
    e['z'] = int(q[0])
    e['x'] = int(q[1])
    e['c'] = int(q[2])
    e['v'] = int(q[3])
    e['b'] = int(q[4])
    if e['z'] + e['x'] + e['c'] + e['v'] + e['b'] == 30 \
    and e['c'] + e['b'] == 14 \
    and e['x'] + e['c'] == 10 \
    and e['v'] - 1 == e['x'] \
        and e['z'] + 1 == e['x'] * 2 :
        print(w)
    
# API and json and request library and interface(email or SMS) jadi 22

import requests
q = requests.get("https://api.jikan.moe/v4/anime/1", \
auth = ("user", "pass"), \
proxies = {"a" : "127.0.0.1:1080"})
print(q)
q.status_code
q.text
q.headers
q.encoding
q.json()
q.json()["data"]
q.json()["data"]["url"]
print("this anime is great and url is", q.json()["data"]["url"])
def s() :
    "API for sending information in my address like my email or sms in my phone"
w = q.json()["data"]["url"]
if w != w :
    print(s)

# define in strings jadi 23

w = "life"
e = 1231415907324.23498
r = 1470
q = "mohammad is revolved in his life now nad he dosn't know about %s and others life" % w
qq = "alireza want to be happy now, he haves %i dollars and is not happy" % r
qqq = "%f peopls lived in this world now" %e
print(q, qq, qqq)

