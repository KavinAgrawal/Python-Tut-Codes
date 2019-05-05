def displayInventory(inventory):
    print('Inventory:')
    num_items=0
    for k,v in inventory.items():
        print(str(v)+' '+k)
        num_items+=v
    print("Total number of items: " + str(num_items))

def addToInventory(inventory, addedItems):
    for v in addedItems:
        inventory[v]=inventory.setdefault(v,0)+1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

    
