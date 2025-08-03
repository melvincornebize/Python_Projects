# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self,day:int, month:int,year:int):
        self.day=day
        self.month=month
        self.year=year
    def __eq__(self, another):
        if self.day==another.day:
            if self.month==another.month:
                if self.year==another.year:
                    return self.year==another.year
                else:
                    return False
            else:
                return False
                if self.year==another.year:
                    return self.year==another.year
                else:
                    return False
        else:
            return False
    def __ne__(self,another):
        return not self==another
    def __gt__(self,another):
        return (self.year,self.month,self.day)>(another.year,another.month,another.day)
    def __ne__(self,another):
        return (self.year,self.month,self.day)!=(another.year,another.month,another.day)
    def __lt__(self,another):
        return (self.year,self.month,self.day)<(another.year,another.month,another.day)
    def __add__(self,addition):
        new_date=self.day+addition
        new_month=self.month
        new_year=self.year
        while new_date>30:
            new_date-=30
            new_month+=1
            if new_month>12:
                new_month=1
                new_year+=1
        new_date=SimpleDate(new_date,new_month,new_year)
        return new_date
    def __sub__(self,another):
        amount_days=30*self.month+360*self.year+self.day
        amount_days_another=30*another.month+360*another.year+another.day
        return abs(amount_days-amount_days_another)
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
if __name__ == "__main__":      
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)