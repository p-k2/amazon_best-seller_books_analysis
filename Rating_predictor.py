import streamlit as st
import pandas as pd
import pickle
from sidebar import sidebar
from theme import apply_theme

st.set_page_config(page_title="Rating Predictor", layout="wide")
plot_theme = sidebar()
apply_theme(plot_theme)
st.markdown(f"""
    <h1 style='color: {"#fffafa"}; font-size: 2.5em;'>🤖 Predict Book Rating</h1>
""", unsafe_allow_html=True)

# Load dataset for reference
df = pd.read_csv("data/bestseller.csv")
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Load pre-trained model
# model = pickle.load(open("models/rating_model.pkl", "rb"))

# User inputs
price = st.number_input("Book Price ($):", min_value=0.0, value=15.0)
year = st.slider("Publication Year:", int(df["Publication Year"].min()), int(df["Publication Year"].max()), 2020)
genre = st.selectbox("Select Genre:", df["Genre"].unique())

# Predict button
if st.button("Predict Rating"):
    # Example: use dummy logic since model not trained here
    predicted_rating = min(5.0, max(1.0, 3.5 + (price-20)/20))  # dummy
    st.success(f"📈 Predicted Rating: {predicted_rating:.2f} ⭐")
