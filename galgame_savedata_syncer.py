import os
import time
import datetime as dt
import numpy as np
import filecmp
from pathlib import Path
import shutil


def check_path_availablity(folder_path: str):
    return os.path.exists(folder_path)


def get_the_most_recent_time_(folder_path):
    files = os.listdir(folder_path)

    the_most_recent_date = max(
        [os.path.getmtime(f"{folder_path}\{f}") for f in files]
    )
    print(time.ctime(the_most_recent_date))
    return the_most_recent_date


def create_backup(folder_path):
    pass


if __name__ == "__main__":
    from config import Config
    paths = Config.paths
    # calculate the files intergrity
    cmp_res = filecmp.cmpfiles(paths[0], paths[1], common=os.listdir(paths[0]))
    if len(cmp_res[1]) + len(cmp_res[2]) == 0:
        print("all file are already been synced to the latest")
        exit()
    # calculate the sync direction
    the_modified_dates = [get_the_most_recent_time_(p) for p in paths]
    the_recentest_cdate = dt.datetime.fromtimestamp(
        max(the_modified_dates)).strftime("%d-%m-%Y--%H-%M")
    the_recentest_path = np.argmax(the_modified_dates)
    print(
        f"{paths[the_recentest_path]} is the most recent modified folder in network")
    sender = paths[the_recentest_path]
    # create a backup for the folder to be synced
    for receiver in paths:
        if receiver == sender:
            continue
        print(f"{receiver} <--- {sender}")
        path = Path(receiver)
        parent_path = path.parent.absolute()
        backup_path = path.joinpath(parent_path, Path("backup_points"))
        if not os.path.exists(backup_path):
            print(f"Create a new backup folder at {backup_path}")
            os.mkdir(backup_path)
        backup_point_path = path.joinpath(
            backup_path, Path(the_recentest_cdate))
        # os.mkdir(backup_point_path)
        shutil.copytree(receiver, backup_point_path)
    # copy the files
        shutil.copytree(sender, receiver, dirs_exist_ok=True)
