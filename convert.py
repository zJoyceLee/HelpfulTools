import os
from PIL import Image


src_path = os.path.join("input")
out_path = os.path.join("output")


def convert(path, folder_name):
    images = []
    for i in os.listdir(path):
        if i.endswith("png") or i.endswith("jpg"):
            images.append(Image.open(os.path.join(path, i)).convert("RGB"))
    print(len(images))
    images[0].save(os.path.join(out_path, "{}.pdf".format(folder_name)), save_all=True, append_images=images[1:])


if __name__ == '__main__':
    for folder in os.listdir(src_path):
        if folder == "input" or folder == "output" or folder.startswith("."):
            continue
        if not os.path.isdir(os.path.join(src_path, folder)):
            continue
        print(folder)
        convert(os.path.join(src_path, folder), folder)
