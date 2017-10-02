#!/bin/bash

# read commit name and push to master all changes

read commitname
git add *
git commit -m $commitname

#!/bin/expect
spawn git push -u origin master
expect "*sername*"
send -- "nikhil12321"

expect "*assword*"
send -- "1234pass"
