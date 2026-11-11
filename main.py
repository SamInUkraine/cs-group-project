# Власник: роль 4 — запуск, тестові дані, звіт, перевірки

from bike import Bike, Station
from client import Client
from rental import take_bike, return_bike, calc_cost, get_total_revenue


def print_report(stations):
    # Друкує звіт адміністратора: скільки велосипедів на кожній станції
    # і скільки мережа заробила загалом (get_total_revenue())
    pass


def run_checks():
    # 2–3 перевірки через assert, наприклад:
    # calc_cost(Bike(99, True), 10) == 50
    # calc_cost(Bike(98, False), 10) == 20
    # take_bike на порожній станції повертає "no_bikes"
    pass


def main():
    # 1. Створити 2 станції: Station("А"), Station("Б")
    # 2. Створити 5 велосипедів (звичайні й електричні) і поставити їх на станції
    # 3. Створити 2 клієнтів: Client("Оля", 300), Client("Петро", 100)
    # 4. Провести 3+ поїздки: take_bike(...), return_bike(...) — і надрукувати результат
    # 5. Спробувати взяти велосипед на порожній станції -> надрукувати зрозуміле повідомлення
    # 6. Надрукувати баланси клієнтів
    # 7. print_report(...)
    # 8. run_checks()
    pass


if __name__ == "__main__":
    main()