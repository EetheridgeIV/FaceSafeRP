#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Error!" >&2
    echo "usage: ./send_photo.sh [file_path]" >&2
    exit 125
else
    file_path=$1
    server_response=`curl -F "picture=@$file_path" https://dj-frsafe.herokuapp.com/upload/`
    echo $server_response
fi
