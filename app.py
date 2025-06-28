<<<<<<< HEAD
import streamlit as st
import pandas as pd
import base64

# --- CONFIG ---
st.set_page_config(
    page_title="Salt Spring Data Services",
    page_icon="🧹",
    layout="centered",
)

# --- LOGO & BRANDING ---
# Load your logos
logo_white_path = "t.png"
logo_black_path = "ty.png"

# Choose which logo based on theme
if st.get_option("theme.base") == "dark":
    logo_path = logo_black_path
else:
    logo_path = logo_white_path

st.image(logo_path, width=300)

# --- TITLE & INTRO ---
st.markdown(
    """
    <h1 style='color:#64dd17; font-family:sans-serif;'>Salt Spring Ltd. Data Services</h1>
    <p style='font-size:18px; color:#555;'>
        Upload your customer or listing data below and receive a cleaned, standardized file ready for use.
        <br><br>
        Our AI-enhanced cleaning ensures consistent headers and smoother data handling.
    </p>
    """,
    unsafe_allow_html=True
)

# --- EMAIL CAPTURE ---
st.markdown("### Enter your email to receive updates or offers:")

email = st.text_input("Email", placeholder="you@example.com")

if email:
    st.success(f"✅ Thanks! We'll keep in touch at **{email}**.")

# --- FILE UPLOAD ---
st.markdown("## Upload Your Data File")

uploaded_file = st.file_uploader(
    "Choose an Excel (.xlsx) or CSV (.csv) file:",
    type=['xlsx', 'csv']
)

if uploaded_file:
    # Load file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully! ✅")
    st.markdown("### Preview of Uploaded Data:")
    st.dataframe(df.head(), use_container_width=True)

    # Data cleaning example: lowercase column names
    cleaned_df = df.copy()
    cleaned_df.columns = [col.lower().strip() for col in cleaned_df.columns]

    st.markdown("---")
    st.markdown("### Preview of Cleaned Data:")
    st.dataframe(cleaned_df.head(), use_container_width=True)

    # Create downloadable CSV
    csv = cleaned_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv",
        use_container_width=True,
    )

else:
    st.info("Upload a file above to start.")

# --- FOOTER ---
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:#888;'>
        &copy; 2025 Salt Spring Ltd. | <a href='mailto:info@saltspringltd.com'>info@saltspringltd.com</a>
    </p>
    """,
    unsafe_allow_html=True
)
=======
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
>>>>>>> b5206aa3c62687945e8cd57fd80113e8eb371691
