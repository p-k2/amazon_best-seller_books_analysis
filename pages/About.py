import streamlit as st
from streamlit_lottie import st_lottie
import requests
from sidebar import sidebar

styles = sidebar()
st.markdown("""
    <style>
        /* Hide Streamlit's default multi-page menu */
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Function to load animation ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load animation ---
lottie_book = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_m9zragkd.json")

# --- Page Title ---

st.title("📖 About the Project")
st.markdown("---")

# --- Animation ---
st_lottie(lottie_book, height=250, key="about_anim")

# --- Section: Project Description ---
st.subheader("🚀 Project Overview")
st.write("""
This project analyzes and visualizes data from the **Amazon Bestseller Books Dataset** 📚.  
It explores author trends, genre performance, and rating distributions — helping understand what makes a book a bestseller.  

The dashboard was built using:
- 🐍 **Python (Pandas, NumPy, Plotly)**
- 🌐 **Streamlit** for interactive web UI
- 🎨 **Custom Themes and Lottie Animations** for better visuals
""")

# --- Section: Data Source ---
st.subheader("📊 Data Source")
st.write("""
The dataset used for this project was downloaded from **[Kaggle](https://www.kaggle.com/)**,  
which provides Amazon's top-selling books data including:
- Title  
- Author  
- User Rating  
- Price  
- Genre  
- Publication Year  
""")

# --- Section: Developer Info ---
st.markdown("---")
st.subheader("👩‍💻 About the Developer")
st.write("""
Hi, I’m **Palakdeep Kaur**, a B.Tech CSE student passionate about **Data Science, Web Development, and Machine Learning**.  
I love combining data and design to build projects that are both **insightful and visually appealing**. 💡  

This project helped me practice:
- Data cleaning and EDA using Pandas  
- Building a dashboard with Streamlit  
- Deploying data-driven apps with interactivity  
""")

st.markdown(
    """
    💻 Check out the project repository here:  
    👉 [GitHub: amazon_best-seller_books_analysis](https://github.com/p-k2/amazon_best-seller_books_analysis)
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Footer ---
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ by Palakdeep Kaur</p>",
    unsafe_allow_html=True
)
