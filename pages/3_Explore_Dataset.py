import streamlit as st
import pandas as pd
from sidebar import sidebar

st.set_page_config(page_title="Explore Dataset", layout="wide")
st.markdown("""
    <style>
        /* Hide Streamlit's default multi-page menu */
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
plot_theme = sidebar()

# Load dataset
df = pd.read_csv("data/bestseller.csv")
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

st.title("🔎 Explore Dataset")

# # Sidebar filters
# selected_genre = st.sidebar.multiselect("Select Genre:", options=df["Genre"].unique(), default=df["Genre"].unique())
# selected_year = st.sidebar.slider("Select Publication Year:",
#                                   int(df["Publication Year"].min()),
#                                   int(df["Publication Year"].max()),
#                                   (int(df["Publication Year"].min()), int(df["Publication Year"].max())))

st.markdown("Use the filters below to explore books by genre and publication year 👇")

# Create columns for filters (for better layout)
col1, col2 = st.columns([2, 1])

with col1:
    selected_genre = st.multiselect(
        "Select Genre:",
        options=df["Genre"].unique(),
        default=df["Genre"].unique()
    )

with col2:
    selected_year = st.slider(
        "Select Publication Year:",
        int(df["Publication Year"].min()),
        int(df["Publication Year"].max()),
        (int(df["Publication Year"].min()), int(df["Publication Year"].max()))
    )
st.markdown("---")
# Apply filters
filtered_df = df[(df["Genre"].isin(selected_genre)) &
                 (df["Publication Year"].between(selected_year[0], selected_year[1]))]

# Show filtered data
st.dataframe(filtered_df)

# Download filtered data
st.download_button(
    "📥 Download Filtered Data",
    filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_data.csv",
    mime="text/csv"
)