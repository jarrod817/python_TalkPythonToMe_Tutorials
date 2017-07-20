import os
import platform
import cat_service
import subprocess


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('---------------------------')
    print('       Cat Factory')
    print('---------------------------')
    # print(__file__) full path
    # print(os.path.dirname(__file__)) path less this file name


def get_or_create_output_folder():
    folder = 'cat pictures'
    full_path = os.path.join(os.path.dirname(__file__), folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Making directory at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    cat_count = 8
    print('Connecting to server to download cats :)')
    for i in range(cat_count):
        name = 'lolcat_{}'.format(i + 1)
        print('Downloading {}'.format(name))
        cat_service.get_cat(folder, name)


def display_cats(folder):
    # open folder
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


if __name__ == '__main__':
    main()
