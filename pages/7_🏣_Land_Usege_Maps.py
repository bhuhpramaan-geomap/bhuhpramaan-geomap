import streamlit as st
import pandas as pd
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

st.title("Land Usage Map")

st.markdown(
    """The land usage map of Bangalore from 2000 to 2023 reveals significant changes and developments in the city's landscape. In 2000, Bangalore, often referred to as the "Garden City," had a balanced distribution of green spaces, residential areas, and industrial zones. Over the years, rapid urbanization has led to a substantial reduction in green cover and agricultural land, replaced by expanding residential and commercial complexes. The growth of the IT sector has spurred the development of numerous tech parks and infrastructure projects. By 2023, Bangalore's landscape showcases a bustling urban environment with a dense network of roads and metro lines, reflecting its evolution into a major metropolitan hub."""
)

m = leafmap.Map()
before_raster = "https://github.com/rajuceg/Geo-Map/raw/main/2000.tif"
after_raster= "https://github.com/rajuceg/Geo-Map/raw/main/2023.tif"
m.split_map(
        left_layer=before_raster, right_layer=after_raster, left_label="2000", right_label="2023"
    )

m.to_streamlit(height=800)

st.markdown(
    """This is Some Land Use Data From 2000 Vs 2023 Reports """
)

file_path = "https://github.com/rajuceg/Geo-Map/raw/main/Land%20Usage%20Category%20Dind.csv"

df = pd.read_csv(file_path)

st.dataframe(df)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)