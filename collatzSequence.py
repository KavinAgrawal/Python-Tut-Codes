def collatz(number):
    if number==1:
        return
    elif number%2==0:
        print(number//2)
        collatz(number//2)        
    else:
        print(3*number+1)
        collatz(3*number+1)
user=int(input())
collatz(user)
