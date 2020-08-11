import streamlit as st
import zipfile
import re
import json
import pandas as pd
from pathlib import Path

st.set_option("deprecation.showfileUploaderEncoding", False)
base = Path("/dgx/github/StreamUp/data/raw_data")
uploaded_file = st.file_uploader("Choose a zip file...")
if uploaded_file:
    with zipfile.ZipFile(uploaded_file, "r") as f:
        f.extractall("/dgx/github/StreamUp/data/raw_data")

# 指定したフォルダ名に従っているか？


# 指定したファイル名に従っているか？
pattern = re.compile(r"\d+_\d{4}_\d{4}_\d{8}.json")
for p in base.glob("jsons/*"):
    result = pattern.match(p.name)
    if result.group():
        continue
    else:
        st.write("error")

pattern = re.compile(r"\d+_\d{4}_\d{4}_\d{8}.bmp")
for p in base.glob("images/*"):
    result = pattern.match(p.name)
    if result.group():
        continue
    else:
        st.write("error")


# json file の stem は必ず bmp file の stem に含まれるか？
images = [p.stem for p in base.glob("images/*.bmp")]
for p in base.glob("jsons/*"):
    if p.stem in images:
        continue
    else:
        st.write("error")

# json file 内で指定していないラベルを付けていないか？
label_list = ["toubu_kizu"]
for p in base.glob("jsons/*"):
    with open(p) as f:
        data = json.load(f)
    for shape in data["shapes"]:
        if shape["label"] in label_list:
            continue
        else:
            st.write(shape["label"])


# 撮像角度は全て同一か？
di = {"stem": [p.stem for p in base.glob("images/*.bmp")]}
df = pd.DataFrame(di)
df["product"] = df["stem"].apply(lambda x: x.split("_")[0])
product_counts = df["product"].value_counts()
if len(product_counts.unique()) != 1:
    st.write("error")
