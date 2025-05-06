"""
Save data
"""

from PySide6.QtWidgets import QInputDialog, QMessageBox
from pathlib import Path
import os
import json


def save_data_json(viewer):
    if not viewer.nome_file:
        QMessageBox.critical(None, "Warning", "No image loaded")
        return

    # ask for code
    code, ok = QInputDialog.getText(
        None,
        "Enter individual info",
        "Code and date (CODE_NN_YYYY-MM-DD):",
        text=viewer.code,
    )
    if not ok:
        QMessageBox.information(
            None,
            "Warning",
            "Data not saved",
        )
        return
    if not code:
        QMessageBox.critical(None, "Warning", "The individual code is mandatory")
        return

    # ask for mass
    mass_value, ok = QInputDialog.getDouble(
        None,  # parent widget
        "Enter the mass value",  # dialog title
        "Mass (in g):",  # label text
        value=viewer.mass_value,  # default value
        minValue=0.0,  # minimum allowed value
        maxValue=100.0,  # maximum allowed value
        decimals=2,  # number of decimal places
    )

    if not ok:
        QMessageBox.information(
            None,
            "Warning",
            "Data not saved",
        )
        return

    data = {
        "mass_value": mass_value,
        "code": code,
        "angle_deg": viewer.angle_deg,
        # "image_file_name": viewer.nome_file,
        # "directory_path": viewer.DIR_PNG,
        "scale": viewer.scale,
        "scale_unit": viewer.scale_unit,
        "landmarks": viewer.landmarks,
        "semilandmarks": viewer.semilandmarks,
    }
    print(f"{data=}")

    json_file_path = viewer.file_path.parent / Path(code).with_suffix(".json")

    try:
        with open(json_file_path, "w") as f_in:
            json.dump(data, f_in, indent=0)
        QMessageBox.information(
            None,
            "Information",
            f"Data saved in {json_file_path}",
        )

        # rename image file
        viewer.file_path.rename(
            viewer.file_path.parent / Path(code).with_suffix(".jpg")
        )

    except Exception as e:
        QMessageBox.critical(None, "Warning", str(e))
