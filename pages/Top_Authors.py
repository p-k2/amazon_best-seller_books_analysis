import streamlit as st
import pandas as pd
from visualizations import top_authors_chart
from sidebar import sidebar

st.set_page_config(page_title="Top Authors", layout="wide")
st.markdown("""
    <style>
        /* Hide Streamlit's default multi-page menu */
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
plot_theme = sidebar()  # ✅ Reusable sidebar with theme

df = pd.read_csv("data/bestseller.csv")
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

author_counts = df['Author'].value_counts()

st.title("👨‍💻 Top 10 Selling Authors")
st.plotly_chart(top_authors_chart(author_counts, plot_theme), use_container_width=True)

st.download_button(
    "📥 Download Top Authors CSV",
    author_counts.head(10).to_csv().encode("utf-8"),
    file_name="top_authors.csv",
    mime="text/csv"
)