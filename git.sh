#!/bin/bash
# read commit name and push to master all changes

echo "commit name:"
read commit_name
git add *
git commit -m $commit_name

git push -u origin master
