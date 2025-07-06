import pandas as pd
import random
from datetime import datetime, timedelta
from geopy.distance import geodesic

bhopal_locations = {
    'MP Nagar': (23.2336, 77.4326),
    'Habibganj': (23.2237, 77.4414),
    'BHEL': (23.2738, 77.5011),
    'Kolar': (23.1824, 77.4197),
    'New Market': (23.2297, 77.3955),
    'Railway Station': (23.2599, 77.4173),
    'Airport': (23.2841, 77.3379),
    'Lalghati': (23.2795, 77.3791),
    'Shahpura': (23.2097, 77.4575),
    'Indrapuri': (23.2643, 77.4897),
    'Ashoka Garden': (23.2665, 77.4237)
}

def calculate_distance(p1, p2):
    return round(geodesic(bhopal_locations[p1], bhopal_locations[p2]).km, 2)

def generate_data(n=3000):
    data = []
    for _ in range(n):
        pickup = random.choice(list(bhopal_locations.keys()))
        drop = random.choice([loc for loc in bhopal_locations if loc != pickup])
        distance = calculate_distance(pickup, drop)
        time = datetime.now() - timedelta(minutes=random.randint(0, 100000))
        hour = time.hour
        dayofweek = time.weekday()
        demand = random.randint(20, 100)
        base_fare = 40
        per_km = 12
        competitor_fare = base_fare + (distance * per_km) + random.randint(-30, 50)
        event = random.choice([0, 1])

        fare = base_fare + distance * per_km
        if demand > 80:
            fare *= 1.4
        elif demand > 50:
            fare *= 1.2
        if event:
            fare *= 1.25

        # Adjust for competitor
        if competitor_fare > fare:
            fare += 0.3 * (competitor_fare - fare)
        else:
            fare -= 0.2 * (fare - competitor_fare)

        data.append([pickup, drop, hour, dayofweek, event, demand, distance, round(competitor_fare, 2), round(fare, 2)])

    return pd.DataFrame(data, columns=[
        'pickup', 'drop', 'hour', 'dayofweek', 'event',
        'demand', 'distance', 'competitor_fare', 'fare'])