"""
Save data
"""


def save_data_json(viewer):
    d = {
        "angle_deg": viewer.angle_deg,
        "image_file_name": viewer.nome_file,
        "directory_path": viewer.DIR_PNG,
        "scale": viewer.scale,
        "scale_factor": viewer.scale_factor,
        "landmarks_groups": viewer.landmarks_groups,
        "semilandmarks": viewer.semilandmarks,
    }
    print(f"{d=}")
