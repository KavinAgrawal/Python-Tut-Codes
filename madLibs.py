#! python3
#enter adjective,noun,adverb or verb which willbe shown in file

import re
addFile=open('File.txt')
readFile=addFile.read()
newFile=open('NewFile.txt','w')
findWord=re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
while findWord.search(readFile)!=None:
    k=findWord.search(readFile).group()
    if k=="ADJECTIVE":
        print('Enter an ADJECTIVE:')
        ADJECTIVE = input()
        readFile= findWord.sub(ADJECTIVE,readFile,1)

    elif k == "NOUN":
        print('Enter a NOUN:')
        NOUN = input()
        readFile = findWord.sub(NOUN, readFile,1)

    elif k == "ADVERB":
        print('Enter an ADVERB:')
        ADVERB =  input()
        readFile= findWord.sub(ADVERB, readFile,1)

    elif k == "VERB":
        print('Enter a VERB:')
        VERB = input()
        readFile= findWord.sub(VERB, readFile,1)
        
print(readFile)
newFile.write(readFile)
newFile.close()
addFile.close()
