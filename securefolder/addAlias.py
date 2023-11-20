import shutil

if __name__ == "__main__":
    shutil.copyfile("/home/msg5/.bashrc", "bashRCbackup.txt")
    additionToBashRC = open("bashfunctionoverwrites.txt", "r").read()
    with open("/home/msg5/.bashrc", "a") as f:
        f.write(additionToBashRC) # add alias here then replace ./bashrc
        f.close()
