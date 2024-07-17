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
    .custom-radio .stRadio label {
        font-weight: bold;
        font-size: 16px;
        color: #4F8BF9;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("LAND USE AND LAND COVER (LULC) OF BANGALORE CITY - A GEOSPATIAL APPROACH")

st.title("Land Usage Map")

st.markdown(
    """The land usage map of Bangalore from 2000 to 2023 reveals significant changes and developments in the city's landscape. In 2000, Bangalore, often referred to as the "Garden City," had a balanced distribution of green spaces, residential areas, and industrial zones. Over the years, rapid urbanization has led to a substantial reduction in green cover and agricultural land, replaced by expanding residential and commercial complexes. The growth of the IT sector has spurred the development of numerous tech parks and infrastructure projects. By 2023, Bangalore's landscape showcases a bustling urban environment with a dense network of roads and metro lines, reflecting its evolution into a major metropolitan hub."""
)

# Create columns
col1, col2 = st.columns([6, 1])

# Define the raster files for each year
raster_files = {
    "2000": "https://github.com/rajuceg/Geo-Map/raw/main/2000.tif",
    "2010": "https://github.com/bhuhpramaan-geomap/bhuhpramaan-geomap/raw/main/2010.tif",
    "2020": "https://github.com/bhuhpramaan-geomap/bhuhpramaan-geomap/raw/main/2020.tif",
    "2023": "https://github.com/rajuceg/Geo-Map/raw/main/2023.tif"
}

# Place the map in the left column
with col1:
    m = leafmap.Map()
    
    # Use custom radio buttons for the right column
    with col2:
        st.markdown("### Select the year of your choice")
        
        st.markdown('<div class="custom-radio">', unsafe_allow_html=True)
        selected_year_for_left = st.radio("Year for Left Map", list(raster_files.keys()), index=0)
        selected_year_for_right = st.radio("Year for Right Map", list(raster_files.keys()), index=1)
        st.markdown('</div>', unsafe_allow_html=True)

    # Get the selected raster files
    before_raster = raster_files[selected_year_for_left]
    after_raster = raster_files[selected_year_for_right]
    
    # Add the split map
    m.split_map(
        left_layer=before_raster, right_layer=after_raster,
        left_label=selected_year_for_left, right_label=selected_year_for_right
    )
    m.to_streamlit(height=500)
