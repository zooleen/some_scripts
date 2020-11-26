#!/bin/bash

LIST=$1

while IFS= read -r host
do
    ./check_redirect.py $host ezaem
done < $LIST
