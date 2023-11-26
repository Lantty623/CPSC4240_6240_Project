#! /user/bin/bash
echo "Adding scripts to ~/.bashrc"
python3 $(CURDIR)/securefolder/addAlias.py
echo "creating a /bin directory in home"
mkdir ~/bin
echo "copying hashtest.py and securefolder.py scripts to current folder and renaming"
echo "changing permissiong to 744 for both"
chmod 744 $(CURDIR)/securefolder/securefolder.py
chmod 744 $(CURDIR)/securefolder/hashtest.py
echo "moving securefolder and hashtest to ~/bin"
cp $(CURDIR)/securefolder/securefolder.py ~/bin/securefolder
cp $(CURDIR)/securefolder/hashtest.py ~/bin/hashtest
echo "should be good to go!"
