import subprocess
from tkinter import *

class CommandHandler:
    """ CommandHandler Class
    Handles all the terminal commands.

    Attributes
    ----------------
    None

    Functions
    ------------------
    moveFile(self, export_path: str, file_name: str):
        Calls a bash script to move all files from the temp folder to the specified directory

    downloadFromURL(self, url: str, export_path: str, file_name: str, progress_lbl: Label, convert_btn: Button):
        Uses subprocess's wsl to download the provided YouTube using yt-dlp
    """

    def __init__(self) -> None:
        """ CommandHandler Constructor
        """
        pass

    def moveFile(self, export_path: str):
        """ 
        Calls a bash script to move all files from the temp folder to the specified directory.

        Parameters
        ----------------
        export_path - string:
        The directory where the newly downloaded mp3 files should be moved to.

        Returns
        ----------------
        None
        """
        export_path = export_path.replace('\\', '\\\\')
        command = ['wsl', './move_files.sh', export_path] 

        subprocess.run(command)
        pass

    def downloadFromURL(self, url: str, export_path: str, file_name: str, progress_lbl: Label, convert_btn: Button) -> None:
        """
        Uses subprocess's wsl to download the provided YouTube using yt-dlp

        Parameters
        ----------------
        url - string:
        The url link to the YouTube video to download audio from

        export_path - string:
        The directory for the audio file after it's downloaded.

        file_name - string:
        The new name for the file when it is downloaded.

        progress_lbl - Label:
        Reference to the progress text on the GUI

        convert_btn - Button:
        Reference to the convert button on the GUI

        Returns
        -----------------
        None
        """
        yt_dlp_command = ['wsl', '../bin/yt-dlp', '--ffmpeg-location', '../bin/ffmpeg', '--extract-audio', '--audio-format', 'mp3', '-o', f'../temp/{file_name}.mp3', f"{url}"]
        
        process = subprocess.Popen(yt_dlp_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        convert_btn.configure(state="disabled")

        for line in process.stdout:
            print(line)
            progress_lbl.configure(text=f"{line}")

        process.wait()
        convert_btn.configure(state="normal")

        if (process.returncode != 0):
            progress_lbl.configure(text=f"YT-DLP Error")
        else:   
            progress_lbl.configure(text=f"Download Finished!")
            self.moveFile(export_path, file_name)