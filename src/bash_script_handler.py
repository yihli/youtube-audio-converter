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

    def moveFile(self, export_path: str, file_name: str):
        # TODO: write the bash script to move to the desired location
        export_path = export_path.replace('\\', '\\\\')
        command = ['wsl', './move_files.sh', export_path] 

        subprocess.run(command)
        pass

    def downloadFromURL(self, url: str, export_path: str, file_name: str, progress_lbl: Label, convert_btn: Button) -> None:
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







        
        