from tkinter import *
from tkinter import filedialog
from bash_script_handler import CommandHandler
import requests
import os
import threading


class YoutubeToAudio:

    def __init__(self, width: int, height: int) -> None:
        # Info 
        # ---------------------------------------
        self.width = width
        self.height = height

        # Class initializations
        # --------------------------------------
        self.root = Tk()
        self.script_handler = CommandHandler()

        # Root GUI Elements
        # --------------------------------------
        self.lbl = Label
        self.file_entry = Entry
        self.video_url_entry = Entry
        self.choose_dir_button = Button
        self.convert_btn = Button
        self.file_entry_lbl = Label
        self.line = Label
        self.line2 = Label
        self.progress_text = Label

        # Status Variables
        # -------------------------------------
        self.programIsRunning = False

    def isValidExportPath(self, export_path: str) -> bool:
        return os.path.exists(export_path) and os.path.isdir(export_path)
    
    def isValidYoutubeURL(self, url: str) -> bool:

        if "youtube.com/watch?v=" not in url:
            print("does not contain youtube.com/watch?v=")
            return False

        
        try: 
            response = requests.head(url, timeout=5, allow_redirects=False)
        except (requests.RequestException, requests.Timeout) as error:
            print("link no work")
            return False
        
        return True
    
    # def toggleButton(self) -> None:
    #     if self.programIsRunning:
    #         self.convert_btn.configure(state="disabled")
    #     else:
    #         self.convert_btn.configure(state="normal")

    def isValidFileName(self) -> bool:
        pass

    def getExportPath(self) -> str:
        return self.file_entry.get()
    
    def getVideoURL(self) -> str:
        return self.video_url_entry.get()
    
    def getFileName(self) -> str:
        return self.file_name_entry.get()
    
    def chooseExportPath(self) -> None:
        export_path = filedialog.askdirectory()
        self.file_entry.delete(0, END)
        self.file_entry.insert(0, f"{export_path}")


    def changeProgressText(self, text) -> None:
        self.progress_text.configure(text=f"{text}")
        
    def cleanURL(self, url: str) -> str:
        if 'https://' not in url:
            url = 'https://' + url

        if '&list' in url: 
            index = url.find('&list')
            url = url[:index]
            print(url)
        return url

    def cleanExportPath(self, export_path: str) -> str:
        if not export_path:
            export_path = "./"
        elif not export_path[-1] == '/':
            export_path += '/'
        
        return export_path
    
    def handleConversion(self) -> None:
    
        # check if the export path is valid
        # check if video can be downloaded 
        video_url = self.getVideoURL()
        export_path = self.getExportPath()
        file_name = self.getFileName()

        export_path = self.cleanExportPath(export_path)
        video_url = self.cleanURL(video_url)

        print(export_path)
        print(self.isValidExportPath(export_path))
        print(video_url)
        print(file_name)

        video_url = self.cleanURL(video_url)

        print(f'{export_path}{file_name}.mp3')


        # if self.isValidYoutubeURL(video_url):
        #     self.convert_btn.configure(state="disabled")
        #     self.thread = threading.Thread(target=self.script_handler.downloadFromURL, args=(video_url, export_path, file_name, self.progress_lbl), daemon=True)
        #     self.thread.start()
        thread = threading.Thread(target=self.script_handler.downloadFromURL, args=(video_url, export_path, file_name, self.progress_lbl, self.convert_btn), daemon=True)
        thread.start()

    
                               
    def initializeGUI(self) -> None:
        # Window creation
        # ---------------------------------
        self.root.title('YouTube to Audio Converter')
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.grid_columnconfigure(0, weight=1)

        # Elements
        # ----------------------------------
        self.lbl = Label(self.root, text="Link to Youtube Video")
        self.video_url_entry = Entry(self.root, width=42)
        self.line2 = Label(self.root, text="---------------------------------------")

        self.file_entry_lbl = Label(self.root, text="Path to export directory:")
        self.file_entry = Entry(self.root, width=43)
        self.choose_dir_button = Button(self.root, text="Choose", width=7, command=self.chooseExportPath)
        self.line = Label(self.root, text="---------------------------------------")

        self.file_name_entry_lbl = Label(self.root, text="Audio file name:")
        self.file_name_entry = Entry(self.root, width = 43)
        self.line3 = Label(self.root, text="---------------------------------------")


        self.convert_btn = Button(self.root, text="Convert to mp3", width=15, command= self.handleConversion)
        self.progress_text = Label(self.root, text="Ready to Go!")

        self.progress_lbl = Label(self.root, text="")
    
        # Element position
        # -----------------------------------
        self.lbl.grid(column=0, row=0)
        self.video_url_entry.grid(column=0, row=1)
        self.choose_dir_button.grid(column=0, row=5)
        self.convert_btn.grid(column=0, row=12)
        self.file_entry_lbl.grid(column=0, row=3)
        self.file_entry.grid(column=0, row=4)
        self.line.grid(column=0, row=6)
        self.line2.grid(column=0, row=2)
        self.progress_text.grid(column=0, row=11)
        self.file_name_entry.grid(column=0, row=8)
        self.line3.grid(column=0, row=10)
        self.file_name_entry_lbl.grid(column=0, row=7)
        self.progress_lbl.grid(column=0, row=13)

    def runProgram(self):
        self.root.mainloop()


                    
            
        
     







