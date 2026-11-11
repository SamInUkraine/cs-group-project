
from bike import Bike, Station
from client import Client
from rental import take_bike, return_bike, calc_cost, get_total_revenue
import datetime

class Rental:
    def __init__(self, user_id, bike):
        self.user_id = user_id
        self.bike = bike
        self.start_time = datetime.now()
        self.end_time = None

    def end_rental(self):
        self.end_time = datetime.now()
