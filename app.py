import streamlit as st
from data_generator import bhopal_locations
from model_predictor import predict_fare
import visualizations as vz

st.set_page_config(page_title="Bhopal Dynamic Pricing", layout="wide")
st.title("🚕 Bhopal Cab Pricing Simulator")

st.sidebar.header("🔧 Ride Inputs")
pickup = st.sidebar.selectbox("Pickup Location", list(bhopal_locations.keys()))
drop = st.sidebar.selectbox("Drop Location", [x for x in bhopal_locations if x != pickup])
hour = st.sidebar.slider("Hour of Day", 0, 23, 9)
dayofweek = st.sidebar.selectbox("Day of Week", list(range(7)), format_func=lambda x: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][x])
demand = st.sidebar.slider("Demand Level", 20, 100, 50)
competitor = st.sidebar.slider("Competitor Fare (₹)", 100, 1000, 300)
event = st.sidebar.checkbox("Festival/Event Day?", False)

fare, distance = predict_fare(pickup, drop, hour, dayofweek, int(event), demand, competitor)
st.success(f"Estimated Fare: ₹{fare} for {distance} km")

st.info("Model factors: pickup/drop, distance, demand, hour, event, and competitor price")

# 📊 Charts
st.subheader("📈 Visual Insights")
df = vz.load_data()

col1, col2 = st.columns(2)
with col1:
    st.altair_chart(vz.demand_vs_fare_chart(df), use_container_width=True)
with col2:
    st.altair_chart(vz.route_fare_chart(df), use_container_width=True)