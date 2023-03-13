import numpy as np
import pandas as pd
import streamlit as st
import time

dataset = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSB5F8jSBATdUPeSoxvD4FquT-uEtrBx5IopAejKpLCHf9RrgwwcbrXWbPwi7CdODxO8BcahV3R04dJ/pub?gid=730914547&single=true&output=csv"

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a URL
@st.cache_data
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

# show dataframe
col = st.columns(1)
st.markdown("### Detailed Data View")
df = st.dataframe(df)
