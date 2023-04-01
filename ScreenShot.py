import time
import pyautogui
import tkinter as tk
import os

# Get the current directory
current_dir = os.getcwd()
folder_name = "screenshots"


def screenshot():
    name=int(round(time.time()*1000))
    name = os.path.join(current_dir, folder_name, '{}.png'.format(int(round(time.time()*1000))))
    #time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()
    
    
#screenshot()
root=tk.Tk()
frame=tk.Frame()
frame.pack()

button=tk.Button(
    frame,
    text="Click to ScreeenShot",
    command=screenshot
)

button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text="Quit",
    command=quit
)
close.pack(side=tk.LEFT)


root.mainloop()


    
    