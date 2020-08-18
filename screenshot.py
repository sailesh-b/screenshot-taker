import time
import pyautogui    #used for python screenshot function
import tkinter as tk    #function for gui for this program


def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(2)                               #This def is for saving the screenshot in different names
    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
root.title("screen capturer")
frame = tk.Frame(root)
frame.pack()


button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="Quit",
    command=quit)
close.pack(side=tk.RIGHT)

root.mainloop()
