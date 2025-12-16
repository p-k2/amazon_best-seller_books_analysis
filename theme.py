

import streamlit as st

def apply_theme():
    theme = st.sidebar.radio("🎨 Choose Theme", ["Light", "Dark"], horizontal=True)

    if theme == "Light":
        bg_color = "#f9f9fc"
        text_color = "#222"
        heading_color = "#4A47A3"
        input_bg = "#ffffff"
        input_border = "#cccccc"
        plot_theme = "plotly_white"
    else:
        bg_color = "#353839"
        text_color = "#fffafa"
        heading_color = "#91A2BB"
        input_bg = "#444"
        input_border = "#666"
        plot_theme = "plotly_dark"

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            font-family: 'Segoe UI', sans-serif;
        }}
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stTitle, .stSubheader {{
            color: {heading_color};
        }}

        /* 🎯 Number Input, Slider, Selectbox styling */
        div[data-baseweb="input"] > input {{
            background-color: {input_bg};
            color: {text_color};
            border: 1px solid {input_border};
            border-radius: 6px;
        }}
        div[data-baseweb="slider"] > div {{
            color: {text_color};
        }}
        div[data-baseweb="select"] > div {{
            background-color: {input_bg};
            color: {text_color};
            border: 1px solid {input_border};
            border-radius: 6px;
        }}
        /* 🎯 Download button styling */
button[kind="primary"] {{
    background-color: #4A47A3;
    color: #fffafa;
    border: none;
    border-radius: 6px;
}}
button[kind="primary"]:hover {{
    background-color: #6B66CC;
}}
        </style>
    """, unsafe_allow_html=True)

    return plot_theme
