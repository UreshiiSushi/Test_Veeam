import sys
import schedule
import shutil
import time
import os
from pathlib import Path
from datetime import timedelta
from distutils import file_util, log


def sync_folders(source: Path, copy: Path):
    if not copy.exists():
        copy.mkdir()
    for i in source.glob("**\*"):
        if i.is_file():
            copied = file_util.copy_file(i, copy, update=1)
            if copied[1]:
                print(f"copied {i.absolute()} to {copy.absolute()}")
    for j in copy.glob("**\*"):
        if j.is_file():
            if not (j.name in os.listdir(source)):
                print(f"deleting {j.name} from {j.absolute()}")
                os.remove(j)
            

    # check existing of copy folder
    # if not : make new folder and copy all files from source
    # if yes : check files


# def set_sync_period(period: timedelta, source: Path, copy: Path):
#     schedule.every(period).seconds.do(main)


def main():
    try:
        source_path = Path(sys.argv[1])
    except IndexError:
        return "No source path entered"

    try:
        copy_path = Path(sys.argv[2])
    except IndexError:
        return "No copy path entered"

    try:
        # period = timedelta(minutes=float(sys.argv[3]))
        period = int(sys.argv[3])
    except IndexError:
        print("No time period entered")
    except ValueError:
        print("Period is not a number")

    if not source_path.exists():
        print("Source path does not exists")

    sync_folders(source_path, copy_path)
    
    # set_sync_period(period, source_path, copy_path)

    print("All ok")


if __name__ == "__main__":
    run_counter = 0
    result = main()
    # schedule.every(int(sys.argv[3])).seconds.do(main)
    # while True:
    #     schedule.run_pending()
    #     run_counter += 1
    #     if run_counter == 9:
    #         break
    #     time.sleep(1)
