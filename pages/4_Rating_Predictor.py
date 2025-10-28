import streamlit as st
import pandas as pd
import pickle
from sidebar import sidebar 

st.set_page_config(page_title="Rating Predictor", layout="wide")
st.markdown("""
    <style>
        /* Hide Streamlit's default multi-page menu */
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
plot_theme = sidebar()

st.title("🤖 Predict Book Rating")

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