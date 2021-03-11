import os
import string
import random
import datetime


def get_file_name(filepath):
    size = 8
    chars = string.ascii_uppercase + string.digits
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    name = ''.join(random.choice(chars) for _ in range(size))

    # print(name)
    return name, ext


def upload_image_path(instance, filename):
    # print(type(instance).__name__)
    date = datetime.datetime.now()
    name, ext = get_file_name(filename)
    new_name = f"{name}{ext}"

    if type(instance).__name__ == "Slider":
        return f"slider/{date.year}/{date.month}/{date.day}/{new_name}"
    elif type(instance).__name__ == "Product":
        return f"product/{date.year}/{date.month}/{date.day}/{new_name}"
    elif type(instance).__name__ == "Blog":
        return f"Blog/{date.year}/{date.month}/{date.day}/{new_name}"
