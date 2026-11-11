from bike import Bike, Station
from client import Client
from rental import take_bike, return_bike, calc_cost, get_total_revenue


def print_report(stations):
    print("=== Звіт ===")
    for station in stations:
        print(f"Станція {station.name}: {station.get_bikes_count()} велосипедів")
    print("Електровелосипеди з низьким зарядом:")
    for station in stations:
        for bike in station.get_low_charge_bikes():
            print(f"Велосипед №{bike.bike_id} - станція {station.name}, заряд {bike.charge}%")
    print(f"Мережа заробила загалом: {get_total_revenue()} грн")


def ride(client, start, finish, minutes):
    status = take_bike(client, start)
    if status == "no_bikes":
        print(f"Вибачте, {client.name}, на станції {start.name} немає придатних велосипедів")
        return
    elif status == "already_riding":
        print(f"Вибачте, {client.name}, спочатку треба повернути велосипед")
        return

    bike = client.current_bike
    status, cost = return_bike(client, finish, minutes)
    if status == "ok":
        print(f"{client.name}: велосипед №{bike.bike_id}, "
              f"Поїдка з {start.name} до {finish.name}, {minutes} хв, списано {cost} грн")
    elif status == "not_enough_money":
        print(f"{client.name}, не вистачає грошей. Поїздка коштує {cost} грн, а на балансі лише {client.balance} грн")
        return



def checks():
    assert calc_cost(Bike(99, True), 10) == 50
    assert calc_cost(Bike(98, False), 10) == 20
    assert take_bike(Client("Тест", 100), Station("Порожня")) == "no_bikes"
    print("Всі перевірки пройдено")


def main():
    khreshchatyk_station = Station("Хрещатик")
    podil_station = Station("Поділ")

    bike_1 = Bike(1, is_electric=False)
    bike_2 = Bike(2, is_electric=True, charge=15)
    bike_3 = Bike(3, is_electric=False)
    bike_4 = Bike(4, is_electric=True, charge=100)
    bike_5 = Bike(5, is_electric=False)

    khreshchatyk_station.add_bike(bike_1)
    khreshchatyk_station.add_bike(bike_2)
    podil_station.add_bike(bike_3)
    podil_station.add_bike(bike_4)
    podil_station.add_bike(bike_5)

    olya = Client("Оля", 300)
    petro = Client("Петро", 100)

    print("=== Поїздки ===")
    ride(olya, khreshchatyk_station, podil_station, 20)
    ride(petro, khreshchatyk_station, podil_station, 15)
    ride(petro, podil_station, khreshchatyk_station, 15)
    ride(olya, podil_station, khreshchatyk_station, 10)

    print("=== Баланси ===")
    print(f"{olya.name}: {olya.get_balance()} грн")
    print(f"{petro.name}: {petro.get_balance()} грн")

    print("")
    print_report([khreshchatyk_station, podil_station])

    checks()


if __name__ == "__main__":
    main()