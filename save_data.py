"""
Save data
"""

def save_data_json(viewer):
    d = {
        "angle_deg":  viewer.angle_deg,
        "image_file_name":  viewer.nome_file
           }
    print(f"{d=}")
    
