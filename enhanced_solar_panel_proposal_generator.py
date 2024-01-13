
import streamlit as st
import matplotlib.pyplot as plt

def calculate_savings(size, consumption, efficiency=0.15, electricity_price=1.5):
    '''
    Calculate the estimated savings from installing solar panels.
    - size: size of the solar panel installation in square meters
    - consumption: average monthly energy consumption in kWh
    - efficiency: efficiency of the solar panels (default is 15%)
    - electricity_price: price of electricity per kWh in SEK (default is 1.5 SEK)
    '''
    annual_production = size * 1000 * efficiency * 1.1  # Assuming 1100 kWh/year per kW installed
    annual_savings = annual_production * electricity_price
    return annual_savings, annual_production

def calculate_roi(annual_savings, initial_investment):
    '''
    Calculate the Return on Investment (ROI) period.
    - annual_savings: estimated annual savings from solar panels
    - initial_investment: cost of installing the solar panels
    '''
    if annual_savings <= 0:
        return float('inf')  # Infinite ROI if no savings
    return initial_investment / annual_savings

def calculate_environmental_impact(annual_production):
    '''
    Estimate the reduction in carbon emissions.
    - annual_production: estimated annual energy production from solar panels
    '''
    carbon_emission_reduction_per_kwh = 0.4 # Average kg CO2 per kWh for Sweden
    return annual_production * carbon_emission_reduction_per_kwh

# Streamlit application layout
st.title("Solar Panel Proposal Generator for Sweden")

st.write("This tool helps you estimate the financial and environmental benefits of installing solar panels.")

# User inputs
st.header("Please enter your details:")
size = st.number_input("Size of your roof in square meters (m²):", min_value=10, max_value=1000, value=50)
consumption = st.number_input("Average monthly energy consumption in kWh:", min_value=100, max_value=2000, value=350)
initial_investment = st.number_input("Initial investment cost for solar panels (in SEK):", min_value=10000, max_value=1000000, value=100000)

# Calculate button
if st.button('Calculate Savings and ROI'):
    savings, production = calculate_savings(size, consumption)
    roi = calculate_roi(savings, initial_investment)
    environmental_impact = calculate_environmental_impact(production)

    st.success(f"Your estimated annual savings: {savings:.2f} SEK")
    st.info(f"Estimated ROI period: {roi:.2f} years")
    st.info(f"Estimated annual reduction in CO2 emissions: {environmental_impact:.2f} kg")

    # Visualization
    fig, ax = plt.subplots()
    ax.bar(['Annual Savings', 'ROI'], [savings, roi], color=['green', 'blue'])
    st.pyplot(fig)

# Note: This script is a prototype. Further development is needed for a full-fledged application.
