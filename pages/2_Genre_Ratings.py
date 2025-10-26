import streamlit as st
import pandas as pd
from visualizations import avg_rating_by_genre_chart
from sidebar import sidebar


st.set_page_config(page_title="Genre Ratings", layout="wide")
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

# Analysis
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()

# Display chart
st.title("⭐ Average Rating by Genre")
st.plotly_chart(avg_rating_by_genre_chart(df, avg_rating_by_genre, plot_theme), use_container_width=True)

# Download button
st.download_button(
    "📥 Download Avg Rating by Genre CSV",
    avg_rating_by_genre.to_csv().encode("utf-8"),
    file_name="avg_rating_by_genre.csv",
    mime="text/csv"
)