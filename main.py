import os
import time

user_home = os.path.expanduser('~')


def find_known_fpath(target_file, starting_dir=user_home):
    """
    Search for a file in a directory and all subdirectories. The starting directory that the program
    starts in is the user's home directory. But you can change this by passing in a different starting
    directory.
    :param target_file: <b>file name to search for, must contain extension.<b>
    :param starting_dir: <b>directory to start search from, defaults to users home path.<b>
    """
    start_time = time.time()
    seeker = os.walk(user_home, topdown=True)
    for dirpath, dirname, filenames in seeker:
        if filenames.__contains__(target_file):
            if len(filenames) > 1:
                for files in filenames:
                    if target_file in files:
                        final_dir = os.path.join(dirpath, files)
                        with open(final_dir, 'r') as f:
                            print(f"Path:{final_dir}\nFile Content: {f.read()}")
            else:
                print(filenames)
                print(f"{os.path.join(dirpath, filenames[0])}")
                final_path = os.path.join(dirpath, filenames[0])
                with open(final_path, 'r') as f:
                    print(f"Path:{final_path}\nFile Content: {f.read()}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Execution time:', round(elapsed_time), 'ms')


find_known_fpath("SECRET.txt")

# def find_known_fpath(path, target_file, target_dir):
#     for dirpath, dirname, filenames in move:
#         if dirpath.__contains__("Desktop") and dirpath.endswith(target_dir):
#             final_path = os.path.join(dirpath, filenames[0])
#             print(final_path)
#
# find_known_fpath(user_home, target_file)
# with open(final_path, "r") as f:
#     print(f.read())
