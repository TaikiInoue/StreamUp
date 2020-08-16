from pathlib import Path

import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image


class UploaderShowDataset:

    base: Path

    def show_dataset(self):

        product_set = set(p.stem.split("_")[0] for p in self.base.glob("dataset/images/*.bmp"))
        product = st.slider(
            label="Product ID", min_value=1, max_value=len(product_set), value=1, step=1,
        )

        stem_list = [p.stem for p in self.base.glob(f"dataset/images/{product}_*.bmp")]
        stem_list = sorted(stem_list)
        i = st.slider(label="Angle", min_value=0, max_value=len(stem_list) - 1, value=0, step=1)
        img = Image.open(self.base / f"dataset/images/{stem_list[i]}.bmp").convert("RGB")
        mask = Image.open(self.base / f"dataset/masks/{stem_list[i]}.png")

        plt.figure(figsize=(9, 3))

        plt.subplot(131)
        plt.imshow(img)
        plt.title("Image")
        plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)

        plt.subplot(132)
        plt.imshow(mask, cmap="Reds")
        plt.title("Mask")
        plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)

        plt.subplot(133)
        plt.imshow(img)
        plt.imshow(mask, cmap="Reds", alpha=0.3)
        plt.title("Supervision")
        plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)

        st.write(f"Stem Name: {stem_list[i]}")
        st.pyplot()
