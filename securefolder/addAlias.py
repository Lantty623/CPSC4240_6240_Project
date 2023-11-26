import shutil
import os

if __name__ == "__main__":
    home_directory = os.path.expanduser("~")
    bashPath = home_directory + "/.bashrc"

    if os.path.exists("securefolder/bashRCbackup.txt"):
        shutil.copy("securefolder/bashRCbackup.txt", bashPath)
    else:
        shutil.copyfile(bashPath, "securefolder/bashRCbackup.txt")

    additionToBashRC = open("securefolder/bashfunctionoverwrites.txt", "r").read()
    with open(bashPath, "a") as f:
        f.write(additionToBashRC) # add alias here then replace ./bashrc
        f.close()
