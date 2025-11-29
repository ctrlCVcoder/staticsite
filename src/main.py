import os
import shutil

from generator import generate_pages_recursive


def copy_directory(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        to_path = os.path.join(dest, filename)
        print(f"Copying {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_directory(from_path, to_path)


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()