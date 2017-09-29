# read commit name and push to master all changes

read commitname
git add *
git commit -m $commitname
git push -u origin master
