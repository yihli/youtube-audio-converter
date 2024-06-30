#!/bin/bash

convertPath () {
    # echo $1
    wslpath -u $1
}

moveFile () {
    newpath=$(convertPath $1)
    mv ../temp/* $newpath
    echo .../temp/* $newpath
}

moveFile $1 

