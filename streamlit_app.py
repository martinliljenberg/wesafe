
import streamlit as st
import requests

def check_health(tenant_name):
    # Normally, you'd call Microsoft Graph API or other APIs here
    # For demonstration, we'll use a mock response.
    api_response = {
        'Azure': 'No Issues',
        'Microsoft 365': 'Minor Issues'
    }
    return api_response

# Streamlit app
st.title('Check Microsoft 365 and Azure Health')

tenant_name = st.text_input('Enter Tenant Name:', '')

if st.button('Check'):
    result = check_health(tenant_name)
    st.write('### Results:')
    st.write(f"Azure: {result['Azure']}")
    st.write(f"Microsoft 365: {result['Microsoft 365']}")
