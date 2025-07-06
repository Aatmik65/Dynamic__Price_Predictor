import pandas as pd
import altair as alt

def load_data():
    return pd.read_csv("training_data.csv")

def demand_vs_fare_chart(df):
    return alt.Chart(df).mark_circle(size=60).encode(
        x='demand', y='fare', color='event:N', tooltip=['pickup', 'drop', 'fare']
    ).interactive().properties(title="Demand vs Fare")

def route_fare_chart(df):
    df['route'] = df['pickup'] + " → " + df['drop']
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('mean(fare):Q', title='Average Fare'),
        y=alt.Y('route:N', sort='-x'),
        color='event:N'
    ).properties(title="Average Fare per Route")
    return chart