import pandas as pd
from data_generator import generate_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

# Generate data
df = generate_data()
le_pickup = LabelEncoder()
le_drop = LabelEncoder()
df['pickup_code'] = le_pickup.fit_transform(df['pickup'])
df['drop_code'] = le_drop.fit_transform(df['drop'])

X = df[['pickup_code', 'drop_code', 'hour', 'dayofweek', 'event', 'demand', 'competitor_fare', 'distance']]
y = df['fare']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor(n_estimators=150, max_depth=10)
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
joblib.dump(le_pickup, 'pickup_encoder.pkl')
joblib.dump(le_drop, 'drop_encoder.pkl')
df.to_csv("training_data.csv", index=False)
