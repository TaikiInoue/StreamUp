from pathlib import Path


class UploaderUpload:

    base: Path
    placeholder: dict

    def upload(self):

        uploaded_file = self.placeholder["uploader"].file_uploader("Choose a zip file...")
        if uploaded_file:
            self.is_uploaded = True
            self.placeholder["upload_status"].success("DONE: Upload")
            return uploaded_file
