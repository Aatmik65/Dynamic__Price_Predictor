import joblib
import pandas as pd
from data_generator import calculate_distance

model = joblib.load('model.pkl')
pickup_enc = joblib.load('pickup_encoder.pkl')
drop_enc = joblib.load('drop_encoder.pkl')

def predict_fare(pickup, drop, hour, dayofweek, event, demand, competitor):
    distance = calculate_distance(pickup, drop)
    pickup_code = pickup_enc.transform([pickup])[0]
    drop_code = drop_enc.transform([drop])[0]

    features = pd.DataFrame([{
        'pickup_code': pickup_code,
        'drop_code': drop_code,
        'hour': hour,
        'dayofweek': dayofweek,
        'event': event,
        'demand': demand,
        'competitor_fare': competitor,
        'distance': distance
    }])
    fare = model.predict(features)[0]
    return round(fare, 2), distance