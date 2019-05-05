def commaSpaceProvider(spam):
    for i in range(len(spam)-1):
        print(spam[i],end=', ')
    print('and',spam[len(spam)-1])
array=['apples', 'bananas', 'tofu', 'cats']
commaSpaceProvider(array)
    
