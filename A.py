n=input()
j=0
term=[]
for i in range(0,int(n)):
    term.append(input())
    j=j+int(term[i])
k=int(2*j/int(n))+1
for i in range(0,int(n)):
    if(k<int(term[i])):
        k=int(term[i])    
print(k)    
    
