#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Error!" >&2
    echo "usage: ./take_photo.sh [UniqueIdentifer]" >&2
    exit 125
else
    UniqueIdentifer=$1
    raspistill -o test$UniqueIdentifer.jpg
    response = `readlink -f test$UniqueIdentifer~.jpg`
    echo $response
fi
