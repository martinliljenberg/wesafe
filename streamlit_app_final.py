
import streamlit as st
import requests
import pandas as pd

def check_health(tenant_name):
    # Normally, you'd call Microsoft Graph API or other APIs here
    # For demonstration, we'll use a mock response.
    api_response = [
        {'Service': 'Azure', 'Status': 'No Issues'},
        {'Service': 'Microsoft 365', 'Status': 'Minor Issues'},
        {'Service': 'Dynamics 365', 'Status': 'Major Issues'}
    ]
    return pd.DataFrame(api_response)

# Streamlit app
st.title('Check Microsoft 365 and Azure Health')

# Layout similar to LinkedIn
col1, col2 = st.columns((1,3))

with col1:
    st.write("## Account Info")
    st.write("Name: John Doe")
    st.write("Tenant: Contoso")

with col2:
    tenant_name = st.text_input('Enter Tenant Name:', '')
    
    if st.button('Check'):
        st.write('## Results:')
        result = check_health(tenant_name)
        st.table(result)
