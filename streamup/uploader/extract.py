import zipfile
from pathlib import Path


class UploaderExtract:

    base: Path
    placeholder: dict

    def extract(self, uploaded_file):

        with zipfile.ZipFile(uploaded_file, "r") as f:
            f.extractall(self.base)
            self.placeholder["extract_status"].success("DONE: Extract")
