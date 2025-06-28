import streamlit as st
import pandas as pd
import base64

# --- CONFIG ---
st.set_page_config(
    page_title="Salt Spring Data Services",
    page_icon="🧹",
    layout="centered",
)

# --- LOGIN SYSTEM ---
# Hard-coded user credentials
USERS = {
    "lucky": "login123",
    "clientA": "clientpass456",
}

# Session state to keep user logged in
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""

# Login Form
if not st.session_state.authenticated:
    st.title("🔐 Login to Salt Spring App")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if username in USERS and USERS[username] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

if st.session_state.authenticated:
    st.sidebar.write(f"✅ Logged in as: {st.session_state.username}")
    st.sidebar.button("Log out", on_click=lambda: st.session_state.update({"authenticated": False}))

    # ------------------------------
    # --- MAIN APP STARTS HERE ----
    # ------------------------------

    # --- LOGO & BRANDING ---
    # Load your logos
    logo_white_path = "t.png"
    logo_black_path = "ty.png"

    # Choose which logo based on theme
    if st.get_option("theme.base") == "dark":
        logo_path = logo_black_path
    else:
        logo_path = logo_white_path

    try:
        st.image(logo_path, width=300)
    except FileNotFoundError:
        st.warning(f"Logo file `{logo_path}` not found. Please check your folder.")

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

    if uploaded_file is not None:
        try:
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

        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

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

else:
    st.info("Please log in to access the app.")
