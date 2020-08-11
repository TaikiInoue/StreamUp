from pathlib import Path
from streamup.uploader import Uploader
import streamlit as st

st.set_option("deprecation.showfileUploaderEncoding", False)


base = Path("/dgx/github/StreamUp/data/raw_data")
uploader = Uploader(base)
