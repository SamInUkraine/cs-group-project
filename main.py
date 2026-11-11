from bike import Bike, Station
from client import Client
from rental import take_bike, return_bike, calc_cost, get_total_revenue


def print_report(stations):
    print("=== Звіт ===")
    for station in stations:
        print(f"Станція {station.name}: {station.get_bikes_count()} велосипедів")
    print(f"Мережа заробила загалом: {get_total_revenue()} грн")
