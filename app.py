import streamlit as st

st.set_page_config(page_title="Embedded Dashboard", layout="wide")

st.title("Embedded Dashboard")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "Rack & POD Dashboard", "Example"])

# --- Main content based on selection ---
if choice == "Home":
    st.header("Home")
    # Two links on Home tab
    st.markdown(
        '<a href="http://example.com/" target="_blank">🔗 Open Example.com</a>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<a href="https://www.wikipedia.org/" target="_blank">📖 Open Wikipedia</a>',
        unsafe_allow_html=True
    )

elif choice == "Rack & POD Dashboard":
    st.markdown(
        '<a href="http://iedubm0app02:8501/" target="_blank">📊 Open Rack & POD Dashboard in new tab</a>',
        unsafe_allow_html=True
    )

    # Clean embed with single scrollbar (iframe only)
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="https://www.wikipedia.org/" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )

elif choice == "Example":
    st.markdown(
        '<a href="http://example.com/" target="_blank">📊 Open Example Dashboard in new tab</a>',
        unsafe_allow_html=True
    )
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="http://example.com/" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )
