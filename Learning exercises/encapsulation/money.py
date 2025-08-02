class Money:
    def __init__(self, euros: int, cents: int):
       
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
  
    def __eq__(self, another):
    
        return self.__euros == another._Money__euros and self.__cents == another._Money__cents

    def __lt__(self, another):
        if self.__euros == another._Money__euros:
            return self.__cents < another._Money__cents
        return self.__euros < another._Money__euros
           
    def __gt__(self, another):
        return not (self < another or self == another)

    def __ne__(self, another):
        return not self == another

    def __add__(self, another):
        new_euros = self.__euros + another._Money__euros
        new_cents = self.__cents + another._Money__cents
        if new_cents >= 100:
            new_cents -= 100
            new_euros += 1
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        total_cents1 = self.__euros * 100 + self.__cents
        total_cents2 = another._Money__euros * 100 + another._Money__cents
        
        if total_cents1 < total_cents2:
            raise ValueError("a negative result is not allowed")
        
        diff_cents = total_cents1 - total_cents2
        
        new_euros = diff_cents // 100
        new_cents = diff_cents % 100
        
        return Money(new_euros, new_cents)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(f"{e1} + {e2} = {e3}")
    print(f"{e1} - {e2} = {e4}")

    try:
        e5 = e2 - e1
    except ValueError as e:
        print(f"Attempting {e2} - {e1} failed: {e}")
