import zipfile
from pathlib import Path


class UploaderZip:

    base: Path
    placeholder: dict

    def save_zip(self, uploaded_file):

        # TODO: Inoue: I have no confidence so here should be confirmed.
        # https://medium.com/dev-bits/ultimate-guide-for-working-with-i-o-streams-and-zip-archives-in-python-3-6f3cf96dca50
        with open(self.base / "dataset.zip", "wb") as f:
            f.write(uploaded_file.getbuffer())

    def extract_zip(self, uploaded_file):

        with zipfile.ZipFile(uploaded_file, "r") as f:
            f.extractall(self.base)
            self.placeholder["extract_status"].success("DONE: Extract")
