#!/usr/bin/expect
spawn "./git.sh"
expect "commit*"
send "regular"
send "\r"
expect "Username*"
send "nikhil12321\r"
expect "Password*"
send "1234pass\r"
