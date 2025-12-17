

import streamlit as st



# def apply_theme():
#     theme = st.sidebar.radio("🎨 Choose Theme", ["Light", "Dark"], horizontal=True)

#     bg_color = "#f9f9fc" if theme == "Light" else "#0E1117"
#     text_color = "#222222" if theme == "Light" else "#FAFAFA"
#     heading_color = "#FFFFFF" if theme == "Dark" else "#4A47A3"
#     input_bg = "#ffffff" if theme == "Light" else "#262730"
#     input_border = "#cccccc" if theme == "Light" else "#3E3E3E"

#     st.markdown(
#         f"""
#         <style>
#         /* 🌙 App background */
#         .stApp {{
#             background-color: {bg_color};
#             color: {text_color};
#         }}

#         /* 🔥 FORCE st.title / st.header / st.subheader */
#         .stApp h1,
#         .stApp h2,
#         .stApp h3 {{
#             color: {heading_color} !important;
#         }}

#         /* Inputs */
#         .stTextInput input,
#         .stTextArea textarea {{
#             background-color: {input_bg};
#             color: {text_color};
#             border: 1px solid {input_border};
#         }}

#         </style>
#         """,
#         unsafe_allow_html=True
#     )
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

