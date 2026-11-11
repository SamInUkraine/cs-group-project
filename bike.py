class Bike:
    def __init__(self, bike_id, is_electric: bool):
        self.bike_id = bike_id
        self.is_electric = is_electric
        self.price_per_min = 5 if is_electric else 2

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
