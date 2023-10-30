
# Import required libraries
import streamlit as st
import openai
import requests
from translate import Translator

# Initialize OpenAI API key (Insert your own API key here)
openai.api_key = "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"

# Function for translating text to Swedish
def translate_to_swedish(text):
    translator = Translator(to_lang="sv")
    return translator.translate(text)

# Function to add custom CSS
def load_css():
    st.markdown("""
    <style>
        h1 {
            color: blue;
        }
        h2 {
            color: green;
        }
        p {
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Function to fetch ROI and business use-cases from OpenAI
def fetch_roi_and_cases(feature_name):
    prompt = f"Tell me the ROI and business use cases for using {feature_name} in a corporate environment."
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

# Function to fetch Microsoft Viva features (Insert the actual URL)
def fetch_viva_features():
    url = "https://techcommunity.microsoft.com/t5/microsoft-viva-blog/what-s-new-in-microsoft-viva-october-2023/ba-p/3949788"
    response = requests.get(url)
    return response.json()  # Assume the response is a JSON object

# Function to generate the newsletter
def generate_newsletter(features, placeholder):
    newsletter_content = "<h1>" + translate_to_swedish("Microsoft Viva Newsletter") + "</h1>"
    for feature in features:
        roi_and_cases = fetch_roi_and_cases(feature["name"])
        translated_roi_and_cases = translate_to_swedish(roi_and_cases)
        newsletter_content += f"""
        <h2>{feature['name']}</h2>
        <p>{translated_roi_and_cases}</p>
        <a href="{feature['link']}">{translate_to_swedish('Learn More')}</a>
        """
    placeholder.markdown(newsletter_content, unsafe_allow_html=True)

# Main function
def main():
    load_css()
    st.title(translate_to_swedish("Microsoft Viva Newsletter Generator"))
    st.subheader(translate_to_swedish("Autonomous Agents by AGI Layer"))

    # Placeholder for the newsletter
    newsletter_placeholder = st.empty()

    # Fetch Viva features
    viva_features = fetch_viva_features()

    if st.button(translate_to_swedish("Generate Newsletter")):
        generate_newsletter(viva_features, newsletter_placeholder)

# Run the app
if __name__ == "__main__":
    main()
