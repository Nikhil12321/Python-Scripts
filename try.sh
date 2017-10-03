#!/usr/bin/expect

#try pushing
set commit_name [lindex $argv 0]
spawn "./git.sh"

expect "enter commit name"
send "$commit_name\r"

expect "Username*"
send "nikhil12321\r"
expect "Password*"
send "1234pass\r"

expect "Branch master set up to track remote branch master from origin."
send "\r"
