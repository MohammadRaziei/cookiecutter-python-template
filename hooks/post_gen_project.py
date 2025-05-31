import os
import shutil
import sys

def move_flat_layout():
    module_name = "{{cookiecutter.module_name}}"
    layout = "{{cookiecutter.layout}}"

    if layout != "flat":
        return  # Do nothing if not flat layout

    src_path = os.path.join("src", module_name)
    dst_path = module_name

    if not os.path.exists(src_path):
        sys.stdout.write(f"Source path {src_path} does not exist. Skipping.\n")
        return

    os.makedirs(dst_path, exist_ok=True)

    for item in os.listdir(src_path):
        s = os.path.join(src_path, item)
        d = os.path.join(dst_path, item)
        shutil.move(s, d)

    try:
        shutil.rmtree("src")
    except Exception as e:
        sys.stdout.write(f"Warning: Failed to remove src folder. Error: {e}\n")

if __name__ == "__main__":
    move_flat_layout()
