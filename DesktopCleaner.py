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

desktop = r"C:\Users\FLAMERKA\Desktop"
za_papka = r"D:\ULTRAPAPKA"
kartinki = r"D:\a\Картинки"
video = r"D:\a\Видео"
zips = r"D:\a\Зипы"
modmain = r"D:\a\модмайн"
progi = r"D:\a\Проги"
text = r"D:\a\текст"
prochee = r"D:\a\прочее"
zvuiki = r"D:\a\Звуки"
else1 = r"D:\a\else1"


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
root.title("DesktopCleaner v1")
root.iconbitmap(r"C:\Users\FLAMERKA\PycharmProjects\flamerkox\venv\DCN.ico")
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
logo = PhotoImage(file="C:\\Users\\FLAMERKA\\PycharmProjects\\flamerkox\\venv\\4.png")
logo2 = Label(root, image=logo, bg="#665873")
logo2.place(x=280, y=0)
logo2.pack()
root.resizable(False, False)
root.mainloop()



