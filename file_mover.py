import os
import shutil
import random
import string

dummy_folders = ["text", "executables", "images", "pdfs", "videos", ]
# extensions = [".txt", ".exe", ".jpg", ".pdf", ".mp4"]
extensions = {"txt": ".txt", "exe": ".exe", "jpg": ".jpg", "pdf": ".pdf", "mp4": ".mp4"}
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
all_files_directory = os.path.join(desktop_path, "allfiles")


def make_all_files_directory():
    os.mkdir(all_files_directory)




def dummy_folder_maker():
    for i in range(len(dummy_folders)):
        os.mkdir(os.path.join(desktop_path, dummy_folders[i]))


def delete_dummy_folders():
    for i in range(len(dummy_folders)):
        os.rmdir(os.path.join(desktop_path, dummy_folders[i]))


def delete_all_files():
    for dummy_files in os.listdir(all_files_directory):
        os.remove(os.path.join(all_files_directory, dummy_files))


def create_random_files():
    for i in range(10):
        with open(
                os.path.join(all_files_directory,
                             f"{''.join(random.choices(string.ascii_letters, k=10))}{random.choice(list(extensions.values()))}"),
                "w") as f:
            pass


def move_files():
    for files in os.listdir(all_files_directory):
        if files.endswith(extensions.get("txt")):
            shutil.move(os.path.join(all_files_directory, files),
                        os.path.join(desktop_path, dummy_folders.__getitem__(0), files))
        elif files.endswith(extensions.get("exe")):
            shutil.move(os.path.join(all_files_directory, files),
                        os.path.join(desktop_path, dummy_folders.__getitem__(1), files))
        elif files.endswith(extensions.get("jpg")):
            shutil.move(os.path.join(all_files_directory, files),
                        os.path.join(desktop_path, dummy_folders.__getitem__(2), files))
        elif files.endswith(extensions.get("pdf")):
            shutil.move(os.path.join(all_files_directory, files),
                        os.path.join(desktop_path, dummy_folders.__getitem__(3), files))
        elif files.endswith(extensions.get("mp4")):
            shutil.move(os.path.join(all_files_directory, files),
                        os.path.join(desktop_path, dummy_folders.__getitem__(-1), files))

# make_all_files_directory()
# dummy_folder_maker()
# create_random_files()
# move_files()
# delete_dummy_folders()
# delete_all_files()

