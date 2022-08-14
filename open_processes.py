import os
from typing import List

import psutil
import traceback
targets = ["Notepad.exe", "Steam.exe"]


def start_all(apps):
    print("Starting all closed apps")
    try:
        for program in apps:
            psutil.Popen(program)
            print(f"starting {program} ...")
    except FileNotFoundError as ex:
        print(f"Application [{program}] could not be started, please check the spelling of the program name.")


def start_processes():
    user_programs = input("Please enter the name of the processes you want to start followed by a comma: ").strip() \
        .split(",")
    running_apps = []
    process_dict = {}
    for proc in psutil.process_iter(['name', 'pid']):
        process_dict[proc.info['name']] = proc.info['pid']
    for k, v in process_dict.items():
        for user_program in user_programs:
            if k == user_program and psutil.pid_exists(v):
                print(f"{k} STATUS: [ALREADY RUNNING]")
                running_apps.append(k)

    closed_apps = list(set(user_programs).difference(running_apps))
    print('=' * 50)
    print(f"Detected closed apps: :{closed_apps}")
    start_all(closed_apps)



start_processes()

