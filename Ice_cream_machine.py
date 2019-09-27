#2. Ice Cream Machine
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        ls = []
        if len(self.ingredients) > 0:
            for i in self.ingredients:
                for j in self.toppings:
                    ls.append([i,j])
        return(ls)

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]