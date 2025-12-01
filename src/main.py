import os
import shutil
import sys
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
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists("docs"):
        shutil.rmtree("docs")

    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()