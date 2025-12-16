
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from sidebar import sidebar

# ---- Page Setup ----
st.set_page_config(page_title="Amazon Bestseller App", page_icon="📘", layout="wide")
st.markdown("""
    <style>
        /* Hide Streamlit's default multi-page menu */
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
# ---- Theme Setup ----
styles= sidebar()


# ---- Load Lottie Animation ----
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_book = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_2glqweqs.json")

# ---- Header Banner ----
st.image("assets/banner_books.jpg",use_column_width=True)

# ---- Title Section ----
st.markdown(
    """
    <h1 style="text-align:center; color:#1E90FF;">📚 Amazon Bestseller Dashboard</h1>
    <p style="text-align:center; font-size:18px;">
        Explore book insights, analyze trends, and discover what makes a book a bestseller.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- Hero Section ----
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
  lot_theme       ### 🚀 Welcome to the Interactive Book Dashboard
        Dive into data of Amazon’s top-selling books to uncover:
        - 🧠 Patterns behind top-rated authors  
        - ⭐ Genre performance and trends  
        - 📈 Data-driven bestseller predictions  

        Use the sidebar to navigate across pages:
        - *🏠 Home*
        - *👑 Top Authors*
        - *⭐ Genre Ratings*
        - *🔍 Explore Dataset*
        - *🤖 Rating Predictor*
        """
    )

with col2:
    st_lottie(lottie_book, speed=1, height=300, key="reading")

st.divider()

# ---- Footer Section ----
st.markdown(
    """
    <div style="text-align:center; margin-top:30px; font-size:15px;">
        Made with 💙 by <b>Palakdeep Kaur</b> <br>
        <i>Amazon Bestseller Books Project</i>
    </div>
    """,
    unsafe_allow_html=True
)