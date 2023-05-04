from glob import glob
from os.path import join
from PIL import Image

import os


def resize_images():
    """
    Resize all images in the folder to the target_size.
    """
    counter = 0
    for img_name in glob(join("../../public/images/thumbnails", "*")):
        img = Image.open(img_name)
        if img.size[0] > 300 and img.size[1] > 300:
            img.thumbnail([300, 300], Image.Resampling.LANCZOS)
            img.save(img_name)
            counter += 1

    print(f"Resized {counter} images.")


def main():
    """
    Convert all .png and .jpg images to .webp in the subfolders.
    """
    resize_images()


if __name__ == "__main__":
    main()
