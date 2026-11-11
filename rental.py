total_revenue = 0

def calc_cost(bike, minutes):
    return minutes * bike.get_price_per_min()

def take_bike(client, station):
    if client.current_bike:
        return "already_riding"

    bike = station.remove_bike()
    if not bike:
        return "no_bikes"

    client.current_bike = bike
    return "ok"

def return_bike(client, station, minutes):
    global total_revenue
    if not client.current_bike:
        return "no_bike", 0

    cost = calc_cost(client.current_bike, minutes)
    if not client.can_pay(cost):
        return "not_enough_money", cost

    client.pay(cost)
    total_revenue += cost
    station.add_bike(client.current_bike)
    client.current_bike = None
    return "ok", cost


def get_total_revenue():
    return total_revenue