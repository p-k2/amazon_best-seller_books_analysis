import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("bestseller.csv")

# Clean data
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)

# Analysis
author_counts = df['Author'].value_counts()
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()

# --- Streamlit UI ---
st.set_page_config(page_title="Bestseller Books Dashboard", layout="wide")

# Title
st.title("📚 Bestseller Books Dashboard")
st.markdown("Welcome to the interactive dashboard for **Amazon Bestseller Books** data. 🎉")

# Quick stats
col1, col2, col3 = st.columns(3)
col1.metric("Total Books", df.shape[0])
col2.metric("Unique Authors", df['Author'].nunique())
col3.metric("Genres", df['Genre'].nunique())

st.markdown("---")

# Top Authors Section
st.subheader("👨‍💻 Top 10 Selling Authors")
st.bar_chart(author_counts.head(10))

# Download button for top authors
st.download_button(
    label="📥 Download Top Authors CSV",
    data=author_counts.head(10).to_csv().encode("utf-8"),
    file_name="top_authors.csv",
    mime="text/csv"
)

st.markdown("---")

# Average Ratings by Genre
st.subheader("⭐ Average Rating by Genre")
st.dataframe(avg_rating_by_genre)

st.bar_chart(avg_rating_by_genre)

# Download button for avg rating
st.download_button(
    label="📥 Download Avg Rating by Genre CSV",
    data=avg_rating_by_genre.to_csv().encode("utf-8"),
    file_name="avg_rating_by_genre.csv",
    mime="text/csv"
)

st.markdown("---")

# Explore dataset with filters
st.subheader("🔎 Explore the Dataset")

# Sidebar filters
st.sidebar.header("Filters")
selected_genre = st.sidebar.multiselect("Select Genre:", options=df["Genre"].unique(), default=df["Genre"].unique())
selected_year = st.sidebar.slider("Select Publication Year:", int(df["Publication Year"].min()), int(df["Publication Year"].max()), (int(df["Publication Year"].min()), int(df["Publication Year"].max())))

# Apply filters
filtered_df = df[(df["Genre"].isin(selected_genre)) & 
                 (df["Publication Year"].between(selected_year[0], selected_year[1]))]

st.dataframe(filtered_df)

st.markdown("✅ Use the sidebar to filter the data and explore trends!")
