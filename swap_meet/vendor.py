from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory = []):
        self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self,category = ""):
        list = []
        
        for item in self.inventory:
            if item.category == category:
                print("item is",Item)
                list.append(item)
        else:
            return list
        return list
    
    
    