import os
import shutil

print("Welcome to COPY_MASTER_100000")


def view_content(directory):
    for files in os.listdir(directory):
        print(files)


def copy_dir():
    """
       Destination directory
       Make sure nothing is wrong with the path by calling absolute path function.
    """
    print("=" * 50)
    user_source_path = input("Enter the source path to be copied: ")
    user_dest_path = input("Enter the destination path: ")
    input(
        "The above action will copy all files from the source path to the destination path.\nPress ENTER to continue.")
    dest = os.path.abspath(user_dest_path)

    """The source directory, which is the directory to be copied to the destination."""
    source = os.path.abspath(user_source_path)

    """
        The final path to the destination directory. example: 
        os.path.join(dest, os.path.basename(source) = C:/Users/Roy/Desktop/dest/source/
        This will copy all files from the source directory to the destination directory.
    """
    final_dest = os.path.join(dest, os.path.basename(source))
    shutil.copytree(source, final_dest, dirs_exist_ok=True, ignore=None)
    print(f"[Moved] {source} -> {final_dest}")
    user_view_content = input("Do you want to view the content of the directory? (y/n): ").lower()
    if user_view_content == "y":
        view_content(final_dest)
    else:
        pass
    while True:
        user_choice = input("Do you want to copy another directory? (y/n): ").lower()
        if user_choice == "y":
            copy_dir()
        elif user_choice == "n":
            print("Thank you for using COPY_MASTER_100000")
            break
        else:
            print("Invalid input. Please enter y or n.")


copy_dir()

# "C:/Users/Roy/Desktop/Plane_Reservation", "C:/Users/Roy/Desktop/dest"
