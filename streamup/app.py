from pathlib import Path

import streamlit as st

from streamup.uploader import Uploader

st.set_option("deprecation.showfileUploaderEncoding", False)


base = Path("/dgx/github/StreamUp/data")
uploader = Uploader(base)
