import streamlit as st

st.set_page_config(page_title="Embedded Dashboard", layout="wide")

st.title("Embedded Dashboard")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "Rack & POD Dashboard", "Example"])

# --- Main content based on selection ---
if choice == "Home":
    st.header("Links")
    # Buttons instead of links
    st.link_button("🔗 Open iFactory", "https://prd.ifactory.dub.corp.jabil.org/home/serializedmaterialviewstandalone#/serializedMaterialViewStandalone/33192493")
    st.link_button("📖 Open Wikipedia", "https://www.wikipedia.org/")
    st.link_button("📊 Rack And POD analytics", "http://iedubm0app02:8501/")
    st.link_button("📈 Dashboard", "http://10.76.48.4/stacktest/v2/dashboard")
    st.link_button("🔍 Process Yield", "http://iedubm0ssrs01/reports/report/Bretton_Test/ProcessYield_Standard_v2")


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
            <iframe src="http://iedubm0app02:8501/" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )
    



http://iedubm0app02:8501
