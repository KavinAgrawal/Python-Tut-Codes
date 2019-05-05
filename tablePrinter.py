def printTable(listType):
    for i in range(len(listType[0])):
        for j in listType:
            print(j[i],end=' ')
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]    
printTable(tableData)
