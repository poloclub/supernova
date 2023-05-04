from glob import glob
from os.path import join
from PIL import Image


def resize_images():
    """
    Resize all images in the folder to the target_size.
    """
    counter = 0
    for img_name in glob(join("../../public/images/thumbnails", "*")):
        img = Image.open(img_name)
        target_length = 300

        if img.size[1] / img.size[0] > 2 or img.size[1] / img.size[0] < 0.5:
            target_length = 600

        if img.size[0] > target_length or img.size[1] > target_length:
            img.thumbnail([target_length, target_length], Image.Resampling.LANCZOS)
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
