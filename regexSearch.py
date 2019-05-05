#!python3
import os,re
k=input('Give the Directory:')
m=input('Give the regex:')
f=os.listdir(k)
for i in f:
    j=open(os.path.relpath(k)+'\\'+i)
    l=j.read()
    c=re.compile(r'%s'%m)
    d=c.findall(l)
    for a in d:
        print(a)
    j.close()    
    
    
