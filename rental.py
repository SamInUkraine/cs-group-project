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

def get_total_revenue():
    return total_revenue