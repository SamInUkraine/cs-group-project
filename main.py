from bike import Bike, Station
from client import Client
from rental import take_bike, return_bike, calc_cost, get_total_revenue


def print_report(stations):
    print("=== Звіт ===")
    for station in stations:
        print(f"Станція {station.name}: {station.get_bikes_count()} велосипедів")
    print(f"Мережа заробила загалом: {get_total_revenue()} грн")


def main():
    khreshchatyk_station = Station("Хрещатик")
    podil_station = Station("Поділ")

    bike_1 = Bike(1, is_electric=False)
    bike_2 = Bike(2, is_electric=True)
    bike_3 = Bike(3, is_electric=False)
    bike_4 = Bike(4, is_electric=True)
    bike_5 = Bike(5, is_electric=False)

if __name__ == "__main__":
    main()