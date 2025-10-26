import streamlit as st
from theme import apply_theme

def sidebar():
    st.sidebar.markdown("## 🧭 Navigation")
    st.sidebar.page_link("main.py", label="Main")
    st.sidebar.page_link("pages/Top_Authors.py", label="👨‍💻 Top Authors")
    st.sidebar.page_link("pages/2_Genre_Ratings.py", label="⭐ Genre Ratings")
    st.sidebar.page_link("pages/3_Explore_Dataset.py", label="🔎 Explore Dataset")
    st.sidebar.page_link("pages/4_Rating_Predictor.py", label="🤖 Rating Predictor")
    st.sidebar.page_link("pages/About.py", label="📖 About me")

    st.sidebar.markdown("---")

    plot_theme = apply_theme()


    st.sidebar.markdown("---")
        # --- FEEDBACK SECTION ---
    st.sidebar.markdown("### 💬 Feedback")
    st.sidebar.info("Found a bug or suggestion?")
    st.sidebar.link_button("📧 Contact Developer", "mailto:your_email@example.com")

    return plot_theme