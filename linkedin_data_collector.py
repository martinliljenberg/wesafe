
# Import required libraries
import streamlit as st
import pandas as pd
import requests
import json
import base64

# Function to get access token from LinkedIn
def get_access_token(client_id, client_secret):
    url = "https://www.linkedin.com/oauth/v2/accessToken"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return json.loads(response.text)['access_token']
    else:
        return None

# Function to fetch LinkedIn data
def fetch_linkedin_data(access_token, company_name):
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://api.linkedin.com/v2/someEndpoint?q={company_name}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

# Streamlit frontend
def main():
    st.title("LinkedIn Data Collector")

    client_id = st.text_input("Enter your LinkedIn Client ID:")
    client_secret = st.text_input("Enter your LinkedIn Client Secret:", type="password")
    company_name = st.text_input("Enter the Company Name:")
    fetch_data = st.button("Fetch Data")

    if fetch_data:
        if client_id and client_secret and company_name:
            access_token = get_access_token(client_id, client_secret)
            if access_token:
                data = fetch_linkedin_data(access_token, company_name)
                if data:
                    st.write("Fetched Data:")
                    st.write(data)
                    # Convert data to DataFrame and show option to download
                    df = pd.DataFrame(data)
                    st.write(df)
                    csv = df.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="{company_name}_data.csv">Download CSV File</a>'
                    st.markdown(href, unsafe_allow_html=True)
                else:
                    st.write("Failed to fetch data.")
            else:
                st.write("Failed to obtain access token.")

if __name__ == "__main__":
    main()
