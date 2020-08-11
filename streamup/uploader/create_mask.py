import json
import labelme
import cv2
import numpy as np
from pathlib import Path


class UploaderCreateMask:

    base: Path
    placeholder: dict

    def create_mask(self):

        Path(self.base / "dataset/masks").mkdir(exist_ok=True)
        label_name_to_value = {"toubu_kizu": 1, "toubu_kizu_outside_marking": 0}
        for p in self.base.glob("dataset/jsons/*"):

            with open(p) as f:
                data = json.load(f)

            label = labelme.utils.shapes_to_label(
                img_shape=(int(data["imageHeight"]), int(data["imageWidth"])),
                shapes=data["shapes"],
                label_name_to_value=label_name_to_value,
            )

            labelme.utils.lblsave(self.base / f"dataset/masks/{p.stem}.png", label)

        # Create masks for images without kizu
        for p in self.base.glob("dataset/images/*.bmp"):

            mask_path = self.base / f"dataset/masks/{p.stem}.png"
            if not mask_path.is_file():
                img = cv2.imread(str(p))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                mask = np.zeros(img.shape, dtype=np.uint8)
                cv2.imwrite(str(mask_path), mask)

        self.placeholder["create_mask_status"].success("DONE: Create Mask from Json")
