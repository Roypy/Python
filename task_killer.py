import os
import subprocess
from typing import *

import psutil

proc_list = psutil.process_iter()


def kill_process(process_name: str):
    for process in proc_list:
        if process.name() == process_name:
            psutil.Popen(["taskkill", "/F", "/IM", process.name()])
            print(f"{process_name} STATUS: [KILLED]")
        elif not process.name() == process_name:
            print("Process not found")
            break




def multi_kill():
    """
    Kill multiple processes

    example:
    multi_kill(["Microsoft.Notes.exe", "Notepad.exe", "Steam.exe"])

    :param processes: List of processes to kill, must include extension.
    :return:
    """
    user_input = input("Please enter the name of the processes you want to kill followed by a comma: ")
    # a new instance of process iter, but it's declared within the local function
    # this is needed because the matching_process list comprehension conflicts with the loops below
    process_list_local = psutil.process_iter()
    matching_processes = [proc.name() for proc in proc_list if proc.name() in user_input.split(",")]

    # Gets the names of the processes that don't match the list of processes
    missing_proc = list(set(user_input.split(',')).difference(matching_processes))
    for process in process_list_local:
        for matching_process in matching_processes:
            if process.name() == matching_process:
                psutil.Popen(["taskkill", "/F", "/IM", process.name()])
                print(f"{matching_process} STATUS: [KILLED]")

    if len(missing_proc) > 0:
        for missing in missing_proc:
            print(f"{missing} STATUS: [NOT FOUND] ")


multi_kill()


def show_processes():
    for process in proc_list:
        print(process.name())

# show_processes()
