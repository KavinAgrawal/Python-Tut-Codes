#! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

   # TODO: Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
           mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower()=='delete' and sys.argv[2] in mcbShelf.keys():
           del mcbShelf[sys.argv[2]]
    
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
           print((str(list(mcbShelf.keys()))))
    elif sys.argv[1].lower() == 'delete':
           for i in list(mcbShelf.keys()):
               del mcbShelf[i]
    elif sys.argv[1] in mcbShelf:
           pyperclip.copy(mcbShelf[sys.argv[1]])
     # TODO: List keywords and load content.
mcbShelf.close()  
