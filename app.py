import streamlit as st

st.set_page_config(page_title="Embedded Dashboard", layout="wide")

st.title("Embedded Dashboard")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "Rack & POD Dashboard", "Example"])

# --- Main content based on selection ---
if choice == "Home":
    st.header("Home")
    # Buttons instead of links
    st.link_button("🔗 Open Example.com", "http://example.com/")
    st.link_button("📖 Open Wikipedia", "https://www.wikipedia.org/")

elif choice == "Rack & POD Dashboard":
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
    # Clean embed with single scrollbar (iframe only)
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="http://example.com/" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )
