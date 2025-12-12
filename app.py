import streamlit as st

st.set_page_config(page_title="Embedded Dashboard", layout="wide")

st.title("Embedded Dashboard")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "Rack & POD Dashboard", "Example"])

# --- Main content based on selection ---
if choice == "Home":
    st.header("Home")
    placeholder_text = "Welcome to the Home tab! This is a placeholder message."
    st.write(placeholder_text)

elif choice == "Rack & POD Dashboard":
    st.markdown(
        '<a href="http://iedubm0app02:8501/" target="_blank">📊 Open Rack & POD Dashboard in new tab</a>',
        unsafe_allow_html=True
    )
    st.components.v1.iframe(
        "https://www.wikipedia.org/",
        height=800,
        width=400
    )

elif choice == "Example":
    st.markdown(
        '<a href="http://example.com/" target="_blank">📊 Open Example Dashboard in new tab</a>',
        unsafe_allow_html=True
    )
    st.components.v1.iframe(
        "http://example.com/",
        height=800,
        width=400
    )
