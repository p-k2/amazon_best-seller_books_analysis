

import streamlit as st


def apply_theme(theme):
    if theme == "Light":
        bg_color = "#f9f9fc"
        text_color = "#222"
        heading_color = "#4A47A3"
        input_bg = "#ffffff"
        input_border = "#cccccc"
        plot_theme = "plotly_white"
    else:
        bg_color = "#353839"
        text_color = "#ffffff"
        heading_color = "#FFFFFF"
        input_bg = "#444"
        input_border = "#666"
        plot_theme = "plotly_dark"


    st.markdown(
    f"""
    <style>
    /* MAIN PAGE */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    /* SIDEBAR CONTAINER */
    section[data-testid="stSidebar"] {{
        background-color: {bg_color} !important;
    }}

    /* SIDEBAR TEXT */
    section[data-testid="stSidebar"] * {{
        color: {text_color} !important;
    }}

    /* TITLES */
    h1, h2, h3 {{
        color: {heading_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

    return plot_theme

