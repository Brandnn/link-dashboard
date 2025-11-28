import streamlit as st

st.set_page_config(page_title="Embedded Dashboard", layout="wide")

st.title("Embedded Dashboard")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "Rack & POD Dashboard", "Embed 2"])

# --- Main content based on selection ---
if choice == "Home":
    st.header("Home")
    # Static placeholder text (not editable)
    placeholder_text = "Welcome to the Home tab! This is a placeholder message."
    st.write(placeholder_text)

elif choice == "Rack & POD Dashboard":
    st.markdown(
        '<a href="http://iedubm0app02:8501/" target="_blank">📊 Open Rack & POD Dashboard in new tab</a>',
        unsafe_allow_html=True
    )
    st.components.v1.iframe(
        "http://iedubm0app02:8501/",
        height=800
    )

elif choice == "Embed 2":
    st.markdown(
        '<a href="http://iedubm0app02:8502/" target="_blank">📊 Open Embed 2 in new tab</a>',
        unsafe_allow_html=True
    )
    st.components.v1.iframe(
        "http://iedubm0app02:8502/",
        height=800
    )
