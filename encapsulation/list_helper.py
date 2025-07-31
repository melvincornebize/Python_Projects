# WRITE YOUR SOLUTION HERE:
#Please create a class named ListHelper which contains the following two class methods.
#greatest_frequency(my_list: list) returns the most common item on the list
#doubles(my_list: list) returns the number of unique items which appear at least twice on the list
#It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:


from collections import Counter
class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list:list):
        counts=Counter(my_list)
        return max(counts, key=counts.get)
    
    @classmethod
    def doubles(cls, my_list:list):
        a=0
        counts=Counter(my_list)
        for key,  value in counts.items():
            if value>=2:
                a+=1
        return a

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))