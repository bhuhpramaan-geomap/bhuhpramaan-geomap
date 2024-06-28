import ast
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


@st.cache_data
def get_layers(url):
    options = leafmap.get_wms_layers(url)
    return options


st.title("Web Map Service (WMS)")
st.markdown(
    """
This app is a demonstration of loading Web Map Service (WMS) layers. Simply enter the URL of the WMS service
in the text box below and press Enter to retrieve the layers. Go to https://apps.nationalmap.gov/services to find
some WMS URLs if needed.
"""
)

row1_col1, row1_col2 = st.columns([3, 1.3])
width = None
height = 600
layers = None

with row1_col2:

    esa_landcover = "https://services.terrascope.be/wms/v2"
    url = st.text_input(
        "Enter a WMS URL:", value="https://services.terrascope.be/wms/v2"
    )
    empty = st.empty()

    if url:
        options = get_layers(url)

        default = None
        if url == esa_landcover:
            default = "WORLDCOVER_2021_S2_TCC"
        layers = empty.multiselect(
            "Select WMS layers to add to the map:", options, default=default
        )
        add_legend = st.checkbox("Add a legend to the map", value=True)
        if default == "WORLDCOVER_2020_MAP":
            legend = str(leafmap.builtin_legends["ESA_WorldCover"])
        else:
            legend = ""
        if add_legend:
            legend_text = st.text_area(
                "Enter a legend as a dictionary {label: color}",
                value=legend,
                height=200,
            )

    with row1_col1:
        m = leafmap.Map(center=[12.971599,77.594566], zoom=9.8)

        if layers is not None:
            for layer in layers:
                m.add_wms_layer(
                    url, layers=layer, name=layer, attribution=" ", transparent=True
                )
        if add_legend and legend_text:
            legend_dict = ast.literal_eval(legend_text)
            m.add_legend(legend_dict=legend_dict)

        m.to_streamlit(width, height)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)