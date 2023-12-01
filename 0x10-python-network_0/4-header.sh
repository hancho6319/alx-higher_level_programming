#!/usr/bin/bash
#Write a Bash script that takes in a URL as an argument
echo -n $(curl -s -H "X-School-User-Id: 98" -X GET "$1")
