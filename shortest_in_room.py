# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons=[]
    def add(self,person:Person):
        self.persons.append(person)
    def is_empty(self):
        if not self.persons:
            return True
        else:
            return False
    def print_contents(self):
        for i in self.persons:
            print(f"{i.name},({i.height}cm)")
    def shortest(self):
        if not self.persons:
            return None
        shortest_person=self.persons[0]
        for persons in self.persons:
            if persons.height<shortest_person.height:
                shortest_person=persons
        return shortest_person
    def remove_shortest(self):
        if not self.persons: 
            return None
        shortest_person=self.persons[0]
        for persons in self.persons:
            if persons.height<shortest_person.height:
                shortest_person=persons
        self.persons.remove(shortest_person)
        return shortest_person
    


        
    
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()