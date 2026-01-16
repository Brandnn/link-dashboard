import streamlit as st

st.set_page_config(page_title="Embedded Dashboard", layout="wide")

st.title("Embedded Dashboard")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Home", "Rack & POD Dashboard", "Example", "ifactory", "Process Yield"])


# Dictionary for link buttons
link_buttons = {
    "🔗 Open iFactory": "https://prd.ifactory.dub.corp.jabil.org/home/serializedmaterialviewstandalone#/serializedMaterialViewStandalone/33192493",
    "📖 Open Wikipedia": "https://www.wikipedia.org/",
    "📊 Rack And POD analytics": "http://iedubm0app02:8501/",
    "📈 Dashboard": "http://10.76.48.4/stacktest/v2/dashboard/",
    "🔍 Process Yield": "http://iedubm0ssrs01/reports/report/Bretton_Test/ProcessYield_Standard_v2/"
}

# --- Main content based on selection ---
if choice == "Home":
    st.header("Links")
    for label, url in link_buttons.items():
        st.link_button(label, url)


elif choice == "Rack & POD Dashboard":
    # Clean embed with single scrollbar (iframe only)
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="http://10.76.48.4/stacktest/v2/dashboard"" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )

elif choice == "Example":
    # Clean embed with single scrollbar (iframe only)
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="https://www.wikipedia.org/" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )


elif choice == "iFactory":
    # Clean embed with single scrollbar (iframe only)
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="https://prd.ifactory.dub.corp.jabil.org/home/serializedmaterialviewstandalone#/serializedMaterialViewStandalone/33192493" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )

elif choice == "Process Yield":
    # Clean embed with single scrollbar (iframe only)
    st.components.v1.html(
        """
        <div style="border:2px solid #ccc; border-radius:6px;">
            <iframe src="http://iedubm0ssrs01/reports/report/Bretton_Test/ProcessYield_Standard_v2/" width="100%" height="800" style="border:none;"></iframe>
        </div>
        """,
        height=820
    )
