#! python30

import re
def checkStrength(regex):
    if len(regex)>=8:
        strong1=re.compile(r'[A-Z]+')
        if strong1.search(regex)!=None:
            strong2=re.compile(r'[a-z]+')
            if strong2.search(regex)!=None:
                strong3=re.compile(r'[0-9]+')
                if strong3.search(regex)!=None:
                    return True;
    else:
        return False            
while True:
  text=input();
  if checkStrength(text):
      print('Strong')
  else:
      print('Weak')
