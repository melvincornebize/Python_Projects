# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name):
        self.__name=name
        self.__observation=""
        self.__number_of_observations=0
    def latest_observation(self):
        return self.__observation
    
    def number_of_observations(self):
        return self.__number_of_observations

    def add_observation(self, observation:str):
        
        self.__observation=observation
        if self.__observation=="":
            raise ValueError
        self.__number_of_observations+=1
    
    

    def __str__(self):
        return f"{self.__name}, {self.__number_of_observations} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)


