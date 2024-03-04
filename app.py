# These lines of code are importing Python libraries that will be used in the script:
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")  # Load data

st.header("Vehicles Dashboard")  # Head Tittle

hist_box = st.checkbox("Build a histogram")  # Generate a button
disp_box = st.checkbox("Build a dispersion plot")  # Generate a button


if hist_box:  # Click button
    # Write a msg
    st.write("Creating a histogram for the dataset of car sale advertisements")

    # Creat a histogram
    fig = px.histogram(car_data, x="odometer")

    # Show a interactive plotly
    st.plotly_chart(fig, use_container_width=True)

if disp_box:  # Click button
    # Write a msg
    st.write("Creating a dispersion plot for the dataset of car sale advertisements")

    # Creat a histogram
    fig = px.scatter(car_data, x="odometer", y="price")  # generate a dispersion plot

    # Show a interactive plotly
    st.plotly_chart(fig, use_container_width=True)
