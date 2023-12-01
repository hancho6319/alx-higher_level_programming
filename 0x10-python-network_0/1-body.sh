#!/usr/bin/bash
#Write a Bash script that takes in a URL, sends a GET
curl -s -w "%{http_code}" -o response.txt "$1" | grep -q 200 && cat response.txt
