#!/bin/bash


read -p 'Full Source Path: ' s_path
if [ -z $s_path ] || [[ $s_path != /* ]]
then
    echo "Full Source path is required (eg. /home/cgalab/sessionx)"
    exit 1
fi

read -p 'Prefix name (eg. session1): ' session
if [ -z "$session" ]
then
    echo "Prefix name is required"
    exit 1
fi

cd $s_path

for f in * ; do mv -- "$f" "${session}_${f}" ; done