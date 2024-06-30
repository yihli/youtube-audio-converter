import subprocess

dir = r'C:\Users\yihon\Desktop\CS\projects\youtube-audio-converter\src\lol.mp3'
dir = dir.replace('\\', '\\\\')
command = ['wsl', './move_files.sh', '../temp/lol.mp3' , dir] 
print(command)
subprocess.run(command)