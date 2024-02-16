from PIL import Image
import os


def add_suffix_to_file(file_path, suffix):
    # Split the file path into directory and file name
    directory, filename = os.path.split(file_path)
    # Split the filename into base name and extension
    base_name, extension = os.path.splitext(filename)
    # Add the suffix to the base name
    new_filename = f"{base_name}_{suffix}{extension}"
    # Join the directory and the new filename to get the new file path
    new_file_path = os.path.join(directory, new_filename)
    return new_file_path


def resize_img(input_img, new_size):
    original = Image.open(input_img)
    resized = original.resize(new_size)
    output_img = add_suffix_to_file(input_img, "resized")
    resized.save(output_img)
    print(f"Success! Resized image saved as {output_img} in main directory")


def read_size():
    print("Enter desired size")
    h = int(input("Height : "))
    w = int(input("Width : "))
    return h, w


input_img = "robot.jpg"
h, w = read_size()
new_size = (h, w)

resize_img(input_img, new_size)
