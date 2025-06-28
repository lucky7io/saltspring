import streamlit as st
import pandas as pd

# Page title and layout
st.set_page_config(page_title="Salt Spring Data Upload", layout="centered")

st.title("Salt Spring Data Services")
st.subheader("Upload Your Customer or Listing Data")

# File uploader
uploaded_file = st.file_uploader(
    "Choose an Excel or CSV file",
    type=['csv', 'xlsx']
)

if uploaded_file is not None:
    # Read file into DataFrame
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("File uploaded successfully!")
        st.write("Here’s a preview of your data:")
        st.dataframe(df.head())

        # Simulate "cleaning" by converting all headers to lowercase
        cleaned_df = df.copy()
        cleaned_df.columns = [col.lower() for col in cleaned_df.columns]

        st.write("Sample cleaned data (headers lowercased):")
        st.dataframe(cleaned_df.head())

        # Let user download the cleaned file
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned File",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv'
        )
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a file to begin.")
