# WRITE YOUR SOLUTION HERE:
class Present:

    def __init__(self, name : str, weight:int):
        self.name=name
        self.weight=weight

    def __str__(self):
        return f"{self.name}: ({self.weight}kg)"

class Box:
    def __init__(self):
        self.valeur=[]
        self.poids_total=0
    
    def add_present(self,present:Present):
        self.valeur.append(present.name)
        self.poids_total+=present.weight

    def total_weight(self):
        return int(self.poids_total)


