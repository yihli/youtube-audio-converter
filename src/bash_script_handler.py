import subprocess
from tkinter import *

class CommandHandler:
    """ BashScriptHandler Class
    
    """
    def __init__(self) -> None:
        """ BashScriptHandler Constructor
        
        """
        pass
    
    # def downloadFromURL(self, url: str, export_path: str, file_name: str) -> None:
    #     
    #     subprocess.run(['./bin/yt-dlp', '--ffmpeg-location', './bin/ffmpeg', '--extract-audio', '--audio-format', 'mp3', '-o', f'{export_path}{file_name}.mp3', f"{url}"])

    def openFilePath(self, path: str):
        command = ['explorer.exe', f'{path}']
        subprocess.run(command)

    def downloadFromURL(self, url: str, export_path: str, file_name: str, progress_lbl: Label) -> None:
        yt_dlp_command = ['../bin/yt-dlp', '--ffmpeg-location', '../bin/ffmpeg', '--extract-audio', '--audio-format', 'mp3', '-o', f'{export_path}{file_name}.mp3', f"{url}"]
        
        process = subprocess.Popen(yt_dlp_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)
            progress_lbl.configure(text=f"{line}")

        progress_lbl.configure(text=f"Download Finished!")
        self.openFilePath(export_path)






        
        