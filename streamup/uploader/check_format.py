import re
import pandas as pd
import sys
import json
import streamlit as st
from pathlib import Path


class UploaderCheckFormat:

    base: Path
    placeholder: dict

    def check_format(self):

        self.check_data_structure()
        self.check_file_convention()
        self.check_stem()
        self.check_label_name()
        self.check_camera_angle()
        self.placeholder["check_status"].success("DONE: Check Data Format")

    def check_data_structure(self):
        """
        dataset
        ├── images
        |   └── *.bmp
        └── jsons
            └── *.json
        """

        data_structure = [str(p.relative_to(self.base)) for p in self.base.glob("*/*")]
        if data_structure != ["dataset/jsons", "dataset/images"]:
            self.error(sys._getframe().f_code.co_name)

    def check_file_convention(self):
        """
        Name convention
        - dataset/images/[0-9]+_[0-9]{4}_[0-9]{4}_[0-9]{8}.bmp
        - dataset/masks/[0-9]+_[0-9]{4}_[0-9]{4}_[0-9]{8}.json
        """

        bmp_pattern = re.compile(r"\d+_\d{4}_\d{4}_\d{8}.bmp")
        for p in self.base.glob("dataset/images/*"):
            if not bmp_pattern.match(p.name):
                self.error(sys._getframe().f_code.co_name)

        json_pattern = re.compile(r"\d+_\d{4}_\d{4}_\d{8}.json")
        for p in self.base.glob("dataset/jsons/*"):
            if not json_pattern.match(p.name):
                self.error(sys._getframe().f_code.co_name)

    def check_stem(self):

        img_stems = [p.stem for p in self.base.glob("dataset/images/*.bmp")]
        for p in self.base.glob("dataset/jsons/*"):
            if p.stem not in img_stems:
                self.error(sys._getframe().f_code.co_name)

    def check_label_name(self):

        label_list = ["toubu_kizu"]
        for p in self.base.glob("dataset/jsons/*"):
            with open(p) as f:
                data = json.load(f)
            for shape in data["shapes"]:
                if shape["label"] not in label_list:
                    st.write(shape["label"])

    def check_camera_angle(self):

        di = {"stem": [p.stem for p in self.base.glob("dataset/images/*.bmp")]}
        df = pd.DataFrame(di)
        df["product"] = df["stem"].apply(lambda x: x.split("_")[0])
        product_counts = df["product"].value_counts()
        if len(product_counts.unique()) != 1:
            self.error(sys._getframe().f_code.co_name)
