#!/usr/bin/expect
spawn "./git.sh"
expect "Username*"
send "nikhil12321\r"
expect "Password*"
send "1234pass\r"
