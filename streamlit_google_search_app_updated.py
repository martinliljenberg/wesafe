
import streamlit as st
import requests
import json

def search_google(api_key, cse_id, name):
    # Build the API request URL
    url = f"https://www.googleapis.com/customsearch/v1?q={name}&key={api_key}&cx={cse_id}"
    # Make the API request
    try:
        response = requests.get(url)
        results = json.loads(response.text)
        return results['items'][0]['link']
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    st.title('Name-based Google Search App')
    
    # Take user input
    name = st.text_input("Enter a name:")
    
    # Check if Google API key and CSE ID are set in Streamlit secrets
    api_key = st.secrets.get("google_api_key", "Your_API_Key_Here")
    cse_id = st.secrets.get("google_cse_id", "Your_CSE_ID_Here")

    # Button to initiate search
    if st.button('Search'):
        if api_key == "Your_API_Key_Here" or cse_id == "Your_CSE_ID_Here":
            st.write("Please set your Google API key and CSE ID in Streamlit secrets.")
        else:
            url = search_google(api_key, cse_id, name)
            st.write(f"Top search result for {name}:")
            st.markdown(url)

if __name__ == "__main__":
    main()
