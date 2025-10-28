import streamlit as st

def apply_theme():
    theme = st.sidebar.radio("🎨 Choose Theme", ["Light", "Dark"], horizontal=True)

    if theme == "Light":
        bg_color = "#f9f9fc"
        text_color = "#222"
        heading_color = "#4A47A3"
        plot_theme = "plotly_white"
    else:
        bg_color = "#353839"
        text_color = "#fffafa"
        heading_color = "#91A2BB"
        plot_theme = "plotly_dark"

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            font-family: 'Segoe UI', sans-serif;
        }}
        .stMarkdown h1,.stMarkdown  h2,.stMarkdown  h3, .stTitle, .stSubheader{{
            color: {heading_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    return plot_theme
