# Власник: роль 3 — поїздки, вартість, виручка мережі

total_revenue = 0  # скільки мережа заробила загалом


def calc_cost(bike, minutes):
    return minutes * bike.get_price_per_min()


def take_bike(client, station):
    # Клієнт бере велосипед зі станції.
    # Повертає статус (рядок):
    #   "ok"            — велосипед узято, він записаний у client.current_bike
    #   "already_riding" — у клієнта вже є велосипед
    #   "no_bikes"      — на станції немає велосипедів
    pass


def return_bike(client, station, minutes):
    # Клієнт повертає велосипед на станцію після поїздки на minutes хвилин.
    # Повертає пару (статус, вартість):
    #   ("ok", cost)               — велосипед на станції, гроші списано, виручка зросла
    #   ("no_bike", 0)             — у клієнта немає велосипеда
    #   ("not_enough_money", cost) — велосипед повернуто, але грошей не вистачило
    pass


def get_total_revenue():
    # Повертає total_revenue
    return total_revenue