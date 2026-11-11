class Bike:
    def __init__(self, bike_id, is_electric: bool, charge=100):
        self.bike_id = bike_id
        self.is_electric = is_electric
        self.price_per_min = 5 if is_electric else 2
        self.charge = charge

    def is_available(self):
        if self.is_electric:
            return self.charge >= 20
        else: 
            return True
    
    def get_price_per_min(self):
        return self.price_per_min

class Station:
    def __init__(self, name: str):
        self.name = name
        self.bikes = []

    def add_bike(self, bike: Bike):
        self.bikes.append(bike)

    def remove_bike(self):
        # забирає велосипед зі станції. якщо велосипеди є - 
        # видаляє останній та повертає його. нема - повертає None

        if not self.bikes:
            return None
        return self.bikes.pop()

    def get_bikes_count(self):
        return len(self.bikes)
    

    def remove_bike(self):
        # видає перший придатний велосипед
        for bike in self.bikes:
            if bike.is_available():
                self.bikes.remove(bike)
                return bike
        return None
    
    def get_low_charge_bikes(self):
        # повертає велосипеди з зарядом менше 20
        return [bike for bike in self.bikes if not bike.is_available()]

