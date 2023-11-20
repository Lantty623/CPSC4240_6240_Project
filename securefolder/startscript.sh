#! /user/bin/bash
echo "Adding scripts to ~/.bashrc"
python3 addAlias.py
echo "creating a /bin directory in home"
mkdir ~/bin
echo "copying hashtest.py and securefolder.py scripts to current folder and renaming"
cp securefolder.py ./securefolder
cp hashtest.py ./hashtest
echo "changing permissiong to 744 for both"
chmod 744 securefolder
chmod 744 hashtest
echo "moving securefolder and hashtest to ~/bin"
mv securefolder ~/bin
mv hashtest ~/bin
echo "should be good to go!"
source ~/.bashrc
