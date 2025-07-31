#Project HERE : 

class Item:
    def __init__(self, name:str, weight:int):
        self.__name=name
        self.__weight=weight
    def name(self):
        return self.__name
    def weight(self):
        return self.__weight
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self,max_weight:int):
        self.item_list=[]
        self.max_weight=max_weight
    def weight(self):
        total_weight=0
        for items in self.item_list:
            total_weight+=items.weight()
        return total_weight
    def number_of_items(self):
        return len(self.item_list)
    def add_item(self,item:Item):
        current_weight=self.weight()
        if current_weight+item.weight()<=self.max_weight:
            self.item_list.append(item)
        else:
            pass
    def print_items(self):
        for i in self.item_list:
            print(i)

    def heaviest_item(self):
        if not self.item_list:
            return None
        current_max=self.item_list[0]
        for items in self.item_list:
            weight=items.weight()
            if items.weight()>current_max.weight():
                current_max=items
        return current_max

    def __str__(self):
        num_items=self.number_of_items()
        current_w=self.weight()
        if num_items==1:
            return f"{num_items} item ({current_w} kg)"
        else:
            return f"{num_items} items ({current_w} kg)"

class CargoHold:
    def __init__(self, max_weight:int):
        self.max_weight=max_weight
        self.current_cargo=0
        self.number_suitcases=0
        self.suitcases_list=[]
       
    def add_suitcase(self, suitcase:Suitcase):
        suitcase_weight=suitcase.weight()
        if suitcase_weight+self.current_cargo<self.max_weight:
            self.current_cargo+=suitcase_weight
            self.number_suitcases+=1
            self.suitcases_list.append(suitcase)
    
    def print_items(self):
        for cases in self.suitcases_list:
            cases.print_items()

    def __str__(self):
        remaining_space=self.max_weight-self.current_cargo
        if self.number_suitcases==1:
            return f"{self.number_suitcases} suitcase, space for {remaining_space} kg"
        return f"{self.number_suitcases} suitcases, space for {remaining_space} kg"

if __name__ == "__main__":
    
    hold = CargoHold(100)
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)
    hold.print_items()
