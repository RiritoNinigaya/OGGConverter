import ctypes
import subprocess
import os
import tk
import tkinter
from tkinter import ttk, filedialog
def AskMP3FileOpen():
    str_mp3 = filedialog.askopenfile(mode="r", filetypes=[('MP3 File', '*.mp3'), ('MP4 File', '*.mp4')], title="Please Choose MP3 File to Convert OGG")
    return os.path.abspath(str_mp3.name)

def Main():
    stringlit = AskMP3FileOpen()
    oggname = input("Please Write OGG Name of You're Sound Or Music: ")
    fh = open("NUL","w")
    subprocess.Popen("ffmpeg -i {} -c:a libvorbis {}.ogg".format(stringlit, oggname), stdout = open("output.txt", "w"), stderr = fh)
    fh.close()
    os._exit(40403)

if __name__ == "__main__":
    Main()
