import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Our Website
<https://www.bhuhpramaan.com>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/MWpI4OI.jpeg"
st.sidebar.image(logo)

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 10px; /* Adjust the value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("LAND USE AND LAND COVER (LULC) OF BANGALORE CITY -A GEOSPATIAL APPROACH")

st.title("Split-panel Map")

st.markdown(
    """
    The Split-panel Map allows you to engage with the map both applications in a single map. On the left side, the satellite image of the Sentinal-2 False color composite. On the right side, the land classification of the bangalore contains vegetation,barren land,etc.,
    """
)

m = leafmap.Map(center=[12.971599,77.594566], zoom=9.8)
m.split_map(
    left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
    )
m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
