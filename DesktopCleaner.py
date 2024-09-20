import os
import shutil
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font

photo_type = [".jpeg", ".jpg", ".png", ".tiff", ".webp", ".svg"]
video_type = [".webm", ".mkv", ".flv", ".ogg", ".gif", ".avi", ".wmv", ".mp4", ".m4p", ".m4v"]
audio_type = [".mp3", ".flac", ".m4a", ".wma", ".aac", ".ec3", ".flp", ".mtm", ".wav"]
zip_type = [".zip", ".rar", ".7z", ".pkg", ".z"]
text_type = [".txt", ".rtf", ".pdf", ".doc", ".docx"]
executable_type = [".apk", ".bat", ".bin", ".msi"]
font_type = [".ttf", ".otf", ".fnt", ".fon"]
exe_type = [".exe"]
jar_type = [".jar"]
else_type = [".ai", ".pptx", ".veg", ".docx", ".bak", ".psd", ".mid"]

os.makedirs('a', exist_ok=True)

desktop = os.path.dirname(os.path.realpath(__file__))
os.makedirs(r'a\Картинки', exist_ok=True)
kartinki = f"{desktop}\a\Картинки"
os.makedirs(r'a\Видео', exist_ok=True)
video = f"{desktop}\a\Видео"
os.makedirs(r'a\Зипы', exist_ok=True)
zips = f"{desktop}\a\Зипы"
os.makedirs(r'a\Модмайн', exist_ok=True)
modmain = f"{desktop}\a\Модмайн"
os.makedirs(r'a\Проги', exist_ok=True)
progi = f"{desktop}\a\Проги"
os.makedirs(r'a\Текст', exist_ok=True)
text = f"{desktop}\a\Текст"
os.makedirs(r'a\Прочее', exist_ok=True)
prochee = f"{desktop}\a\Прочее"
os.makedirs(r'a\Звуки', exist_ok=True)
zvuiki = f"{desktop}\a\Звуки"
os.makedirs(r'a\else1', exist_ok=True)
else1 = f"{desktop}\a\else1"


def aboba(path):
    ext = os.path.splitext(path)[1]
    return ext


def compare(file):
    a = aboba(file)
    for file1 in photo_type:
        for file2 in video_type:
            for file3 in zip_type:
                for file4 in executable_type:
                    for file5 in font_type:
                        for file6 in exe_type:
                            for file7 in jar_type:
                                for file8 in else_type:
                                    for file9 in audio_type:
                                        for file10 in text_type:
                                            if a == file1:
                                                return "photo_type"
                                            if a == file2:
                                                return "video_type"
                                            if a == file3:
                                                return "zip_type"
                                            if a == file4:
                                                return "executable_type"
                                            if a == file5:
                                                return "font_type"
                                            if a == file6:
                                                return "exe_type"
                                            if a == file7:
                                                return "jar_type"
                                            if a == file8:
                                                return "else_type"
                                            if a == file9:
                                                return "audio_type"
                                            if a == file10:
                                                return "text_type"



def Move(file, type):
    print("aaaaaaaaaaa")
    if type == "photo_type":
        shutil.move(file, kartinki)
    if type == "video_type":
        shutil.move(file, video)
    if type == "zip_type":
        shutil.move(file, zips)
    if type == "executable_type":
        shutil.move(file, prochee)
    if type == "font_type":
        shutil.move(file, prochee)
    if type == "exe_type":
        shutil.move(file, progi)
    if type == "jar_type":
        shutil.move(file, modmain)
    if type == "else_type":
        shutil.move(file, prochee)
    if type == "audio_type":
        shutil.move(file, zvuiki)
    if type == "text_type":
        shutil.move(file, text)
    else:
        shutil.move(file, else1)

def Clear():
    print("clear")
    for folder, subfolder, files in os.walk(desktop):
        for file in files:
            file = os.path.join(folder, file)
            # if aboba(file) == ".pyw" or ".py":
            #     continue
            try:
                Move(file, compare(file))
                continue
            except FileNotFoundError:
                continue
        return messagebox.showinfo("Success!", "Успешная очистка!!!!")


def Exit():
    sys.exit()




root = Tk()
root.title("DesktopCleaner v0.1")
root.geometry('300x200+780+400')
root.configure(background="#665873")
btn = Button(root, text="Очистить рабочий стол", command=Clear, font="Arial, 18", bg="#463b52", fg="#7b6594")
btn.pack()
btn.place(x=5, y=60)
btn1 = Button(root, text="Выключить программу", command=Exit, font="Arial, 8", bg="#463b52", fg="#7b6594")
btn1.pack()
btn.configure(width=20)
btn1.configure(width=30)
btn1.place(x=100, y=170)
version = Label(root, text="v1", bg="#665873", fg="#463b52")
version.place(x=0, y=180)
logo2.place(x=280, y=0)
logo2.pack()
root.resizable(False, False)
root.mainloop()



