import os
import xml.etree.ElementTree as ET

xml_dir = "DataSet/Sohas_weapon-Detection/annotations_test/xmls"
label_dir = "DataSet/Sohas_weapon-Detection/labels/val"

os.makedirs(label_dir, exist_ok=True)

classes = ["gun", "knife", "pistol"]

def convert_box(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]

    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]

    return (x * dw, y * dh, w * dw, h * dh)

for xml_file in os.listdir(xml_dir):
    if not xml_file.endswith(".xml"):
        continue

    tree = ET.parse(os.path.join(xml_dir, xml_file))
    root = tree.getroot()

    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    txt_file = os.path.join(label_dir, xml_file.replace(".xml", ".txt"))

    with open(txt_file, "w") as f:
        for obj in root.iter("object"):
            cls = obj.find("name").text.lower()

            if cls not in classes:
                continue

            cls_id = classes.index(cls)

            xmlbox = obj.find("bndbox")
            b = (
                float(xmlbox.find("xmin").text),
                float(xmlbox.find("xmax").text),
                float(xmlbox.find("ymin").text),
                float(xmlbox.find("ymax").text),
            )

            bb = convert_box((w, h), b)
            f.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")

print("Validation XML converted successfully!")