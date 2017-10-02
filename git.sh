#!/bin/bash
# read commit name and push to master all changes

echo "commit name"
read commitname

git add *
git commit -m $commitname

git push -u origin master
