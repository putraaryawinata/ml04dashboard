import numpy as np
import pandas as pd
import streamlit as st
import time
from PIL import Image

dataset = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSB5F8jSBATdUPeSoxvD4FquT-uEtrBx5IopAejKpLCHf9RrgwwcbrXWbPwi7CdODxO8BcahV3R04dJ/pub?gid=730914547&single=true&output=csv"

im = Image.open("icon.jpg")
st.set_page_config(
    page_title="Real-Time ML-04 Dashboard",
    page_icon=im,
    layout="wide",
)

# read csv from a URL
# @st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset)

df = get_data()

# dashboard title
st.title("ML-04 Dashboard")

# top-level filters
col1, col2, col3, col4 = st.columns(4)
with col1:
    sort_by = st.selectbox("Sort by", df.columns)
with col2:
    ascending = st.selectbox("Sequence", ["asc", "desc"])

# dataframe filter
ascending = ascending == "asc"
df = df.sort_values(by=sort_by, ascending=ascending)

st.markdown("### Detailed Data View")

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# show table
df = st.table(df)
