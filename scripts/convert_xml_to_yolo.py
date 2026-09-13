import os
import xml.etree.ElementTree as ET

# Paths
xml_folder = "dataset/train/annotations"
label_folder = "dataset/train/labels"

os.makedirs(label_folder, exist_ok=True)

# Class names
classes = [
    "scratches",
    "rolled-in_scale",
    "pitted_surface",
    "patches",
    "inclusion",
    "crazing"
]

for xml_file in os.listdir(xml_folder):

    if not xml_file.endswith(".xml"):
        continue

    xml_path = os.path.join(xml_folder, xml_file)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find("size")
    image_width = int(size.find("width").text)
    image_height = int(size.find("height").text)

    yolo_lines = []

    for obj in root.findall("object"):

        class_name = obj.find("name").text.strip()

        if class_name not in classes:
            continue

        class_id = classes.index(class_name)

        box = obj.find("bndbox")

        xmin = float(box.find("xmin").text)
        ymin = float(box.find("ymin").text)
        xmax = float(box.find("xmax").text)
        ymax = float(box.find("ymax").text)

        # Convert to YOLO format
        x_center = ((xmin + xmax) / 2) / image_width
        y_center = ((ymin + ymax) / 2) / image_height

        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height

        yolo_lines.append(
            f"{class_id} {x_center:.6f} {y_center:.6f} "
            f"{width:.6f} {height:.6f}"
        )

    txt_file = os.path.splitext(xml_file)[0] + ".txt"
    txt_path = os.path.join(label_folder, txt_file)

    with open(txt_path, "w") as f:
        f.write("\n".join(yolo_lines))

print("XML to YOLO conversion completed!")