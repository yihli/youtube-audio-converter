# Imports
# --------------------------
from youtube_to_audio import YoutubeToAudio

# Main
# ------------------------------
def main() -> None:
    yt = YoutubeToAudio(400, 500)
    yt.initializeGUI()
    yt.runProgram()

if __name__ == "__main__":
    main()
