
# Import required libraries
import streamlit as st
import openai
from docx import Document

# Function to call GPT-4 API
def call_gpt4(api_key, prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=200  # Increased token limit for more content
    )
    return response.choices[0].text.strip()

# Function to export text to a Word document
def export_to_word(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save("Generated_Quotation.docx")
    st.success('Exported to Word document as "Generated_Quotation.docx".')

# Streamlit Frontend
def main():
    st.title('Sales Quotation Generator')

    # API Key Input
    gpt4_api_key = st.text_input("Enter your GPT-4 API Key:", type="password")

    # Collecting seller information
    seller_name = st.text_input("Seller Name:")
    customer_name = st.text_input("Customer Name:")
    contact_name = st.text_input("Contact Name:")
    customer_info = st.text_area("Information about the Customer:")
    current_environment = st.text_area("Information about the Customer's Current Environment:")

    # Product selection (Mock Data)
    product_options = ['Product A', 'Product B', 'Product C']
    selected_products = st.multiselect('Select Products:', product_options)

    # Generate Quotation
    if st.button('Generate Quotation'):
        # Create custom prompt for GPT-4
        custom_prompt = f"Create a sales quotation for Microsoft 365 Business Premium.\n\nSeller: {seller_name}\nCustomer: {customer_name}\nContact: {contact_name}\nCustomer Info: {customer_info}\nCurrent Environment: {current_environment}\nSelected Products: {', '.join(selected_products)}"
        
        # Call GPT-4 API
        generated_text = call_gpt4(gpt4_api_key, custom_prompt)
        
        # Display Generated Quotation
        st.subheader("Generated Quotation")
        st.write(generated_text)

        # Button to Export to Word
        if st.button('Export to Word'):
            export_to_word(generated_text)

if __name__ == "__main__":
    main()
