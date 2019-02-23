import os
import platform
import subprocess

import cat_service


def main():
    # print the header
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print(folder)
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def print_header():
    print("-------------------")
    print("   CAT FACTORY")
    print("-------------------")


def get_or_create_output_folder():
    folder = "cat_pictures"
    base_folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at {}".format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = "lolcat_{}".format(i)
        cat_service.get_cat(folder, name)
        print("Downloaded {}".format(name))
    print("Download complete.")


def display_cats(folder):
    print("Displaying cats in OS window.")
    if platform.system() == "Darwin":
        subprocess.call(["open", folder])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", folder])
    elif platform.system() == "Windows":
        subprocess.call(["start", folder], shell=True)
    else:
        print("We don't support your os.")


if __name__ == '__main__':
    main()
