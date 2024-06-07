#!/usr/bin/bash
# Checks if the required command line tools are installed on the user's system.

checkYTDLP() {
    which yt-dlp

    return_code=$?

    if [ ! $return_code -eq 0 ]; then
        exit 1
    fi
}

checkFFMPEG() {
    which ffmpeg

    return_code=$?

    if [ ! $return_code -eq 0 ]; then
        exit 2
    fi
}

checkFFMPEG
exit 0

