from pathlib import Path

import streamlit as st

from streamup.uploader.check_format import UploaderCheckFormat
from streamup.uploader.create_mask import UploaderCreateMask
from streamup.uploader.dvc import UploaderDVC
from streamup.uploader.show_dataset import UploaderShowDataset
from streamup.uploader.status import UploaderStatus
from streamup.uploader.upload import UploaderUpload
from streamup.uploader.zip import UploaderZip


class Uploader(
    UploaderCheckFormat,
    UploaderStatus,
    UploaderUpload,
    UploaderZip,
    UploaderCreateMask,
    UploaderShowDataset,
    UploaderDVC,
):
    def __init__(self, base: Path):

        self.base = base
        self.is_uploaded = True if Path(self.base / "dataset").exists() else False

        if self.is_uploaded:
            self.show_dataset()

        else:
            self.placeholder = {}
            self.placeholder["uploader"] = st.empty()
            self.placeholder["upload_status"] = st.empty().info("UNDO: Upload")
            self.placeholder["extract_status"] = st.empty().info("UNDO: Extract")
            self.placeholder["check_status"] = st.empty().info("UNDO: Check Data Format")
            self.placeholder["create_mask_status"] = st.empty().info("UNDO: Create Mask from Json")

            uploaded_file = self.upload()
            if uploaded_file:
                self.save_zip(uploaded_file)
                self.extract_zip(uploaded_file)
                self.check_format()
                self.create_mask()
                self.data_versioning()
                self.show_dataset()
