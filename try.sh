#!/usr/bin/expect
spawn "./git.sh"
expect "Username*"
send "nikhil12321\r"
expect "Password*"
send "1234pass\r"

expect "Branch master set up to track remote branch master from origin."
send "\r"
